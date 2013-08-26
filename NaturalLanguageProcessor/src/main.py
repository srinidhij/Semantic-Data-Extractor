#!/usr/bin/python
from extract import *
from createc import ParseHtml
from parsein import ParseLp
import sys

def main():

    nmdb = ParseHtml().main()
    name = raw_input('Enter name : \n')
    #print nmdb
    print 'Created databasre of nobel prize winners with %s entries'%str(len(nmdb))
    print 'Searching for %s ...'%name
    pdata = None
    for tn in nmdb:
        #print tn['name']
        if tn['name'].lower() == name.lower():
            pdata = tn
            break
    if pdata == None:
        print 'Name %s Not found'%name
        sys.exit(1)
    print 'Fetching data about %s'%name
    datal = ParseLp(pdata['link']).parse()
    data = '.'.join(datal)
    nex = NEExtract(data)
    #print data
    print nex.main()
if __name__ == '__main__':
    main()