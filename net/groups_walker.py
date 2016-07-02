# coding=utf-8
__author__ = 's.rozhin'

import requests


class GroupLink:
    def __init__(self, group_id, to_name, url, from_group_id, from_name, link_name=''):
        self.link_name = link_name
        self.from_group_id = from_group_id
        self.to_group_name = to_name
        self.from_group_name = from_name
        self.to_group_id = group_id
        self.url = url


class Group:
    def __init__(self, id, name):
        self.Id = id
        self.Name = name
        self.linksFrom = {}
        self.linksTo = {}
        self.link_to_me_count = 0
        self.link_from_me_count = 0

    def add_link_to_me(self, link):
        self.linksTo[link.from_group_id] = link
        self.link_to_me_count += 1

    def add_link_from_me(self, link):
        self.linksTo[link.to_group_id] = link
        self.link_from_me_count += 1


class GroupStorage:
    def __init__(self):
        self.groups = {}

    def add_link(self, link):
        assert isinstance(link, GroupLink)
        if link.from_group_id not in self.groups:
            self.groups[link.from_group_id] = Group(link.from_group_id, link.from_group_name)
        self.groups[link.from_group_id].add_link_from_me(link)
        if link.to_group_id not in self.groups:
            self.groups[link.to_group_id] = Group(link.to_group_id, link.to_group_name)
        self.groups[link.to_group_id].add_link_to_me(link)

    def print_statistics(self):
        for group in sorted(self.groups.itervalues(), key=lambda gr: gr.link_to_me_count, reverse=True):
            print u'{0}\t{1}\t{2}'.format(group.Name, group.link_to_me_count, group.link_from_me_count)


def extract_group_id(group_url):
    if group_url == 'http://vk.com/club_ulyibka':
        return 'club_ulyibka'
    if group_url == 'http://vk.com/ssoplegenda':
        return 'soplegenda'
    if group_url.find("/club") == -1:
        return group_url[group_url.rfind("/") + 1:]
    else:
        return group_url[group_url.rfind("/club") + 5:]


def build_group_links(links_array, from_group_id, from_group_name):
    for raw_group_link in links_array:
        url_ = raw_group_link[u'url']
        group_id = extract_group_id(url_)
        print "url: " + url_
        print "extracted group_id: " + group_id
        if u'desc' in raw_group_link:
            yield GroupLink(group_id, raw_group_link[u'name'], url_, from_group_id, from_group_name,
                            raw_group_link[u'desc'])
        else:
            yield GroupLink(group_id, raw_group_link[u'name'], url_, from_group_id, from_group_name)


def get_links(group_id):
    r = requests.get('https://api.vk.com/method/groups.getById?group_id={0}&fields=links'.format(group_id))
    print r.text
    group_info = r.json()['response'][0]
    group_id = group_info['gid']
    group_name = group_info['name']
    if 'links' not in group_info:
        return []
    else:
        return build_group_links(group_info['links'], group_id, group_name)


link_list = []
visitedSet = set()
group_storage = GroupStorage()

def wide_walk(start_group_id, depth, max_depth):
    if depth > max_depth:
        return
    if start_group_id in visitedSet:
        return

    links = get_links(start_group_id)
    for link in links:
        link_list.append(link)
        group_storage.add_link(link)
        try:
            wide_walk(link.to_group_id, depth + 1, max_depth)
        except:
            print 'Some error for groupId{0}'.format(link.to_group_id)
    visitedSet.add(start_group_id)


def print_link(l):
    print(u'{1} {2} {0} {3}'.format(l.to_group_name, l.link_name, l.to_group_id, l.from_group_id))

wide_walk('sso.festival', 0, 2)
group_storage.print_statistics()
