#!/usr/bin/python
import urllib2,sys

if len(sys.argv) == 2:
	try:
		port = int(sys.argv[1])
	except : 
		print 'Error : port number has to be an integer'
		sys.exit(1)
else :
	port = 8888

site = 'http://localhost:'+str(port)

def main():
	req = urllib2.Request(site, headers={'User-Agent' : "Mozilla/5.0 (Linux; U; Android 4.0.4; en-gb; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"})
	try:
		res = urllib2.urlopen(req)
	except Exception as e :
		print 'Error occured while connecting '+str(e)
		sys.exit(1)
	print res.read()
if __name__ == '__main__':
	main()
