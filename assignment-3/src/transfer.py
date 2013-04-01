from pymongo import *
from colldata import *
from json import dumps

client = MongoClient('localhost',27017)
db = client.WikiPeopleDatabase
wikipeople = db.WikiPeopleDatabase
#f = open('test.db','r')
#t = f.readline().split(';')[:-1]
wikipeople.remove()
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
#for p in t:
	#entry = {}
	#l = p.split(',')
	#for k in l:
		#y = k.split('=')
		#print y
		#if y[0]!="gender":
			#entry[y[0]] = y[1]
	#wikipeople.insert(entry)
#wikipeople.remove()
#temp = wikipeople.find({'year':'2012'})
#print temp