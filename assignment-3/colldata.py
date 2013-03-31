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
def main():
	db = BuildDB()
	data = db.build()
	for dat in data:
		print dat
if __name__ == '__main__':
	main()