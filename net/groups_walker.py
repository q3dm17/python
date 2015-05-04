# coding=utf-8
__author__ = 's.rozhin'

import requests
import xml.etree.ElementTree as ET


def get_links(group_id):
    r = requests.get('https://api.vk.com/method/groups.getById?group_id={0}&fields=links'.format(group_id))
    print r.text
    return r.json()['response'][0]['links']


for group in get_links('sso_taiga'):
    # print group
    if u'desc' in group:
        print(u'{1} {2} {0} {3}'.format(group[u'desc'], group[u'name'], group[u'url'], group['id']))
    else:
        print(u'{0} {1} {2}'.format(group[u'name'], group[u'url'], group['id']))


class Group:
    def __init__(self, id, name, url):
        self.name = name
        self.id = id
        self.url = url