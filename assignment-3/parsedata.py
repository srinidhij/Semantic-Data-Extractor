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
			dat = dict()
			tdatli = re.findall(tdattrpat,trlist[i])
			tdli = re.findall(tdpat,trlist[i])
			if i == 0 or i == 1:
				print tdatli
				print tdli
			invalid = 0
			flag = 0
			for j in tdatli:
				if j != '':
					k = j.strip()
					k = k.split('=')
					try:
						rspan = int(k[1])
						t = (rspan,tdatli.index(j))
						#print rspan
					except:
						#invalid =1
						break
					flag = 1
					break
			#if invalid == 1:
			#	continue
			while flag == 1 and rspan > 0 :
				#year and achievement
				if t[1] == 0:

				rspan -= 1
			for j in tdli:
				'''
				if i == 1:
					#print j
					#print tdatli,'\n\n'
				'''
				#ali = re.findall(apat,j)
				#print ali
			i += 1
		return trlist

if __name__ == '__main__':
	p = HTMLParser(open('test.html').read())
	data =  p.parse()
	#print data[1]