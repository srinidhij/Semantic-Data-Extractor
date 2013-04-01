#!/usr/bin/python
from crawler import Crawler
from parsehtml import HTMLParser

class BuildDB:
        def __init__(self):
                pass
        def build(self):
                cw = Crawler()
                udata = cw.main()
                data = []
                for tdat in udata:
                        parser = HTMLParser(tdat['data'])
                        data += parser.parse(tdat['category'])
                return data
def getData():
        db = BuildDB()
        data = db.build()
        return data
