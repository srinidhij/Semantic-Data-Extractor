import urllib2,sys
site = 'http://localhost:8888'

def main():
	req = urllib2.Request(site, headers={'User-Agent' : "Mozilla/5.0 (Linux; U; Android 4.0.4; en-gb; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"})
	try:
		res = urllib2.urlopen(req)
	except:
		raise
	print 'asdgasdfgas'
	print res.read()
if __name__ == '__main__':
	main()