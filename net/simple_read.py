__author__ = 's.rozhin'

import urllib2

response = urllib2.urlopen('https://vk.com/audibooks')
from HTMLParser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            # print "Start tag:", tag
            for attr in attrs:
                if 'href' == attr[0] and attr[1].startswith('/'):  # and not attr[1].endswith('#'):
                    print "     attr:", attr[1]


html = response.read()
parser = MyHTMLParser()
parser.feed(html)

