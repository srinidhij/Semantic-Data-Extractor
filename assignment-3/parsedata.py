#!/usr/bin/python
import re
import sys

class HTMLParser:
	def __init__(self,data=None):
		if not data:
			print 'Error : No data was given to parse'
			sys.exit(1)
		self.htmldata = data

	def clean(self):
		self.htmldata = self.htmldata.replace('\n','')
		self.htmldata = self.htmldata.replace('\t','')
		self.htmldata = self.htmldata.replace('"','')
		self.htmldata = self.htmldata.replace('\'','')
		self.htmldata = self.htmldata.replace('(','')
		self.htmldata = self.htmldata.replace(')','')

	def parse(self):
		self.clean()
		htmldata = self.htmldata
		# we are assuming all info is in a table (as is the case most of the times)
		tdpat = re.compile('<td>(.*?)</td>')
		trpat = re.compile('<tr>(.*?)</tr>')
		trlist = re.findall(trpat,htmldata)
		tdattrpat = re.compile('<td(.*?)>')
		apat = re.compile('<a.*>(.*?)</a>')
		if len(trlist) < 1:
			print 'error'
			sys.exit(1)
		del(trlist[0])
		del(trlist[0])
		i=0
		while i<len(trlist):
			tdatli = re.findall(tdattrpat,trlist[i])
			tdli = re.findall(tdpat,trlist[i])
			flag = 0
			for j in tdatli:
				if j != '':
					j = j.strip()
					j = j.split('=')
					try:
						rspan = int(j[1])
					except:
						break
					flag = 1
					break
			while flag ==1 and rspan > 0 :
				#year and achievement
				rspan -= 1
			for j in tdli:
				if i==1:
					print j
					#print tdatli,'\n\n'
					ali = re.findall(apat,j)
					print ali
			
			i += 1
		return trlist

if __name__ == '__main__':
	p = HTMLParser(open('test.html').read())
	data =  p.parse()
	#print data[1]