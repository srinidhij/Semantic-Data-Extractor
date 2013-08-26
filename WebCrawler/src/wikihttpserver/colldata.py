#!/usr/bin/python
from crawler import Crawler
from parsehtml import HTMLParser

class BuildDB:
        ''' Class to build the database from the 
        data parsed by the parser'''
        def __init__(self):
                pass
        def build(self):
                ''' Gets the data from the crawler and uses 
                parser to parse the data and returns the data'''
                cw = Crawler()
                udata = cw.main()
                data = []
                for tdat in udata:
                        parser = HTMLParser(tdat['data'])
                        data += parser.parse(tdat['category'])
                return data
def getData():
        ''' return data got from the parser'''
        db = BuildDB()
        data = db.build()
        return data
