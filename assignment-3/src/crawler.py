import urllib2
import sys

class Crawler:
        
        def __init__(self,ipfile='tocrawl.txt',opfile='output'):
                self.ipfile = ipfile
                self.opfile = opfile
        
        def main(self):
                treadli = open(self.ipfile).read().split("\n")[:-1]
                readli = []
                for tsite in treadli:
                        tdata = dict()
                        tsite = tsite.split('::')
			print tsite
                        if len(tsite) != 2:
                                print 'Error : Invalid crawl list'
                                sys.exit(1)
                        tdata['site'] = tsite[0]
                        tdata['category'] = tsite[1]
                        readli.append(tdata)

                data = []
                for page in readli:
                        try:
                                req = urllib2.Request(page['site'], headers={'User-Agent' : "Magic Browser"})
                        except:
                                print 'Unexpected exception'
                                sys.exit(1)
                        try:
                                res = urllib2.urlopen(req)
                        except urllib2.URLError, e:
                                try:
                                        if e.code == 404:
                                                print 'Error 404 on page %s: page not found'%page
                                                sys.exit(1)
                                        if e.code == 403:
                                                print 'Error 403 on page %s: forbidden'%page
                                                sys.exit(1)
                                except:
                                        print e
                                        sys.exit(1)                
                        sitedata = res.read()
                        temp = {}
                        temp['category'] = page['category']
                        temp['site'] = page['site']
                        temp['data'] = sitedata
                        data.append(temp)       

                of = open(self.opfile,'w')
                of.write(str(data))
                of.close()
                return data

if __name__ == '__main__':
        cr = Crawler()
        print cr.main()
