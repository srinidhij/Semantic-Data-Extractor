#!/usr/bin/python
from BeautifulSoup import BeautifulSoup
from crawler import Crawler    
import cPickle as pickle
import sys

class ParseHtml:
    def main(self):
        try:
            with open('linkdb.pickle'):
                return pickle.load(open('linkdb.pickle'))

        except IOError:
            sys.setrecursionlimit(10000)
            cw = Crawler()
            data = cw.main()
            soup = BeautifulSoup(data)
            dtable = soup.findAll('table')[1]
            drows = dtable.findAll('tr')
            j = 1
            pdata = []
            while j<len(drows):
                drele = dtable.findAll('td')
                k = 1
                while k < len(drele):
                    flag = 0
                    pdict = dict()
                    try:
                        pdict['name'] = drele[k].find('a').contents[0]
                        pdict['link'] = 'http://en.wikipedia.org' + drele[k].find('a')['href']
                    except:
                        flag = 1
                        
                    if flag == 1 :
                        k += 1
                        continue
                    #print pdict
                    pdata.append(pdict)
                    k += 1
                j += 1
            pickle.dump(pdata, open('linkdb.pickle', 'wb'))
            return pdata

def main():
    p = ParseHtml()
    print p.main()
if __name__ == '__main__':
    main()