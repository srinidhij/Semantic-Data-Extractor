#!/usr/bin/python
import sys
import urllib2
class Crawler():
    def main(self):
        site = 'http://en.wikipedia.org/wiki/List_of_Nobel_laureates';
        try:
            req = urllib2.Request(site,headers={'User-Agent' : "Magic Browser"})
            res = urllib2.urlopen(req)
        except urllib2.URLError, e :
            print str(e)
            sys.exit(1)
        data = res.read()
        return data