#!/usr/bin/python
from pymongo import *
from colldata import *
from json import dumps
class CreateDB:
	''' Class to create the database from the 
	data obtained by parser'''

	def create(self):
		'''Create a mongo client and get the data from parser
		and insert the data into the database'''
		client = MongoClient('localhost',27017)
		db = client.WikiPeopleDatabase
		wikipeople = db.WikiPeopleDatabase
		#f = open('test.db','r')
		#t = f.readline().split(';')[:-1]
		wikipeople.remove()
		#get data from the parser
		data = getData()
		print "Data Crawled"
		for d in data:
			entry = {}
			for key,val in d.items():
				if key in ['name','year','country','achievement','category']:
					if not isinstance(val,int):
						temp = ''
						for a in val:
							try:
								temp+=a
							except:
								pass
						entry[key] = temp
						#print 'ny'
					elif isinstance(val,int):
						entry[key] = str(val)
						#print 'y'
			#print ''
			#entry['_id'] = None
			#print entry
			#entry = dumps(entry)
			wikipeople.insert(entry)
def main():
	db = CreateDB()
	db.create()
if __name__ == '__main__':
	main()