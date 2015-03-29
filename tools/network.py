# send_to_address = "vm-cs2"
send_to_address = "localhost"
sendToPort = 2405
import httplib
# conn = httplib.HTTPConnection(send_to_address, sendToPort)
# conn.request("POST", "/certificates/303049EA-7EB8-49D2-9B85-E1D54820FB03/refresh", "")
# resp = conn.getresponse()
# print resp.status


def send_request(uri):
    current_connection = httplib.HTTPConnection(send_to_address, sendToPort, 1, 5)
    current_connection.set_debuglevel(1)
    current_connection.request("POST", uri, "", {"Content-Length": "0"})
    resp = current_connection.getresponse()
    respData = resp.read()
    print uri, resp.status, resp.reason

    current_connection.close()


def process_strings_from_std_in():
    import fileinput

    for line in fileinput.input():
        send_request(line)


uri_list = ["/certificates/79B09E1A-9EB5-48C4-A8F4-B52ED44796BA/refresh",
            "/certificates/303049EA-7EB8-49D2-9B85-E1D54820FB03/refresh",
            "/certificates/79B09E1A-9EB5-48C4-A8F4-B52ED44796BA/refresh"]
for resource in uri_list:
    send_request(resource)
# send_request("/certificates/79B09E1A-9EB5-48C4-A8F4-B52ED44796BA/refresh")
# send_request("/certificates/303049EA-7EB8-49D2-9B85-E1D54820FB03/refresh")
# send_request("/certificates/79B09E1A-9EB5-48C4-A8F4-B52ED44796BA/refresh")
# process_strings_from_std_in()
# conn.close()

