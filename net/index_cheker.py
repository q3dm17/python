import httplib
import requests

__author__ = 's.rozhin'

normal_index_difference = 100


class ReplicaResult:
    def __init__(self, address, size):
        self.size = size
        self.address = address


def ask_replica(address):
    current_connection = httplib.HTTPConnection(address)
    current_connection.set_debuglevel(1)
    current_connection.request("GET", "/sys/indexsize", "", {"Content-Length": "0"})
    resp = current_connection.getresponse()
    respData = resp.read()
    print address, resp.status, resp.reason
    print respData
    current_connection.close()
    return ReplicaResult(address, respData)


def get_replica_list(service_names):
    r = requests.get('http://clusterconfig:9000/default')
    print r.text
    cluster_conf = r.json()
    for service in service_names:
        yield cluster_conf['topology/{0}/'.format(service)]


def check_index(adress_list):
    replica_result_list = []
    index_total_size = 0
    replica_count = 0
    for replica in adress_list:
        replica_result = ask_replica(replica)
        replica_result_list.append(replica_result)
        index_total_size += replica_result.size
        replica_count += 1
    index_average_size = index_total_size / replica_count
    for result in replica_result_list:
        replica_diff = abs(result.size - index_average_size)
        if replica_diff > normal_index_difference:
            yield (replica_result.address, result.size, replica_diff)


for topology_list in get_replica_list(["trels.service", "slaservice"]):
    for topology in topology_list:
        print topology