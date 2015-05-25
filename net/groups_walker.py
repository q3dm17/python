# coding=utf-8
import logging

__author__ = 's.rozhin'

import requests


class GroupLink:
    def __init__(self, group_id, name, url, from_group_id, link_name=''):
        self.link_name = link_name
        self.from_group_id = from_group_id
        self.to_group_name = name
        self.to_group_id = group_id
        self.url = url


class Group:
    def __init__(self, id, name):
        self.Visited = False
        self.Id = id
        self.Name = name


class GroupStorage:
    def __init__(self):
        self.groups = {}

    def visited(self, group_id):
        if group_id not in self.groups:
            return False
        else:
            return self.groups[group_id].Visited

    def add(self, group):
        assert isinstance(group, Group)
        self.groups[group.Id] = group

    def mark_visited(self, group_id):
        self.groups[group_id].Visited = True


def extract_group_id(group_url):
    if group_url.find("/club") == -1:
        return group_url[group_url.rfind("/")+1:]
    else:
        return group_url[group_url.rfind("/club")+5:]


def build_group_links(links_array, from_group_id):
    for raw_group_link in links_array:
        url_ = raw_group_link[u'url']
        group_id = extract_group_id(url_)# better use http_link
        print "url: " + url_
        print "extracted group_id: "+group_id
        if u'desc' in raw_group_link:
            yield GroupLink(group_id, raw_group_link[u'name'], url_, from_group_id,
                            raw_group_link[u'desc'])
        else:
            yield GroupLink(group_id, raw_group_link[u'name'], url_, from_group_id)


def get_links(group_id):
    r = requests.get('https://api.vk.com/method/groups.getById?group_id={0}&fields=links'.format(group_id))
    print r.text
    group_info = r.json()['response'][0]
    group_id = group_info['gid']
    if 'links' not in group_info:
        return []
    else:
        return build_group_links(group_info['links'], group_id)


# for link in get_links('sso_taiga'):
# print(u'{1} {2} {0} {3}'.format(link.to_group_name, link.link_name, link.to_group_id, link.from_group_id))

link_list = []
groupStorage = GroupStorage()


def wide_walk(start_group_id, depth, max_depth):
    groupStorage.mark_visited(start_group_id)
    if depth > max_depth:
        return

    links = get_links(start_group_id) # here use extract_group_id(url_)
    for link in links:
        link_list.append(link)
        if groupStorage.visited(link.to_group_id):
            continue
        else:
            groupStorage.add(Group(link.to_group_id, link.to_group_name))
            wide_walk(link.to_group_id, depth + 1, max_depth)


def print_link(l):
    print(u'{1} {2} {0} {3}'.format(l.to_group_name, l.link_name, l.to_group_id, l.from_group_id))

groupStorage.add(Group("sso_taiga", "atata"))
wide_walk('sso_taiga', 0, 2)
for gr_l in link_list:
    print_link(gr_l)


