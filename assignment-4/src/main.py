#!/usr/bin/python
from extract import *
from createc import ParseHtml
from parsein import ParseLp
import sys

def main():

    nmdb = ParseHtml().main()
    name = raw_input('Enter name : \n')
    print name
    pdata = None
    for tn in nmdb:
        #print tn['name']
        if tn['name'].lower() == name.lower():
            pdata = tn
            break
    if pdata == None:
        print 'Not found'
        sys.exit(1)
    datal = ParseLp(pdata['link']).parse()
    data = '.'.join(datal)
    nex = NEExtract(data)
    print data
    nex.main()
if __name__ == '__main__':
    main()