#!/usr/bin/python
import urllib2
import sys
import re
from BeautifulSoup import BeautifulSoup

class ParseLp:
    def __init__(self,link):
        self.href = link
    def getData(self):
        try:
            req = urllib2.Request(self.href,headers={'User-Agent' : "Magic Browser"})
            res = urllib2.urlopen(req)
        except urllib2.URLError, e :
            print str(e)
            sys.exit(1)
        data = res.read()
        self.data = data
    def parse(self):
        self.getData()
        soup = BeautifulSoup(self.data)
        divs = soup.findAll('div')
        for div in divs:
            if div['id'] == 'bodyContent':
                mdat = div
                break
        texts = div.findAll(text=True)

        def visible(element):
            if element.parent.name in ['style', 'script', '[document]', 'head', 'title'] or element == '\n':
                return False
            elif re.match('<!--.*-->', str(element)):
                return False
            return True

        visible_texts = filter(visible, texts)
        j = 0
        while j<len(visible_texts):
            visible_texts[j] = visible_texts[j].strip(' \n\t')
            j += 1
        return visible_texts

def main():
    site = 'http://en.wikipedia.org/wiki/Wilhelm_R%C3%B6ntgen'
    tp = ParseLp(site)
    print tp.parse()

if __name__ == '__main__':
    main()