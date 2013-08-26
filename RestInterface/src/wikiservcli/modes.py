#!/usr/bin/python
from argparse import ArgumentParser
import string
import random 
import os
import sys
from datetime import datetime as time

def id_generator(chars=string.ascii_lowercase):
	'''Generates random strings of random length'''
	size = random.randrange(4,6)
	return ''.join(random.choice(chars) for x in range(size))

def gen_rand_data(datarange,database,fname):
	'''Generates random entries for the database'''
	i = 0
	f = open(fname,'a')
	while i<datarange:
		e = {}
		name = str(id_generator())+ ' ' +str(id_generator())
		year = random.randrange(1990,2014)
		category = random.choice(['peace','physics','chemistry','literature','economics'])
		achievement = str(id_generator()).strip()
		gender = random.choice(['m','f'])
		country = random.choice(['india','germany','france','usa','england','china','russia','switzerland','australia','spain'])
		e['name'] = name.strip()
		e['year'] = year
		e['category'] = category.strip()
		e['achievement'] = achievement
		e['gender'] = gender
		e['country'] = country.strip()
		f.write("name="+name+",year="+str(year)+",category="+category+",achievement="+achievement+",gender="+gender+",country="+country+";")
		database.append(e)
		i = i + 1
	return database

class Database:
	'''Class for database operations'''
	def serialize(self):
		'''Convert the database object to
		strings for storing in file'''
		dbstr = ''
		for i in self.maindb:
			tstr = ''
			for j in i.keys():
				tstr += j+'='+str(i.get(j,''))+','
			dbstr += tstr[:-1]+';'
		return dbstr

	def printdb(self,p=None):
		'''Print the database or the results
		in suitable format'''
		self.printtime = 0
		start = time.now()
		printData = ''
		if p is None:
			printData+= 'NULL\n'
			return
		keysstr = ''
		if p==[]:
			printData+='NULL\n'
			return
		printData+= '='*120+'\n'
		for j in p[0]:
			keysstr += '%10s'%j + ' '*9
		printData+= keysstr+'\n'
		printData+= ('='*120)+'\n'
		for j in p: 
			astr = ''
			for k in j.keys(): 
				astr += '%12s'%j.get(k,'')+' '*5
			printData+= astr+'\n'
		printData+= ('='*120)+'\n'
		printData+= 'Fetched %s entry(ies)'%(str(len(p)))
		self.printtime = time.now() - start
		printData+= str(self.printtime.seconds+float(self.printtime.microseconds)/1000000)+'\n'
		return printData+'\n'



	def create(self,fname='database.in',rnumber=0):
		'''Read from existing db file and create 
		the database.Also create database using 
		random entries.If the file you specify already exists 
		the new entries will be	appended to the file and 
		original entries will be unchanged.If random entry generatation 
		option is not used then the database will be created using 
		the entries present in the file'''
		self.creattime=0
		start = time.now()
		self.dbstr=''
		self.maindb=[]
		maindb = self.maindb
		self.filename = fname
		
		if os.path.exists(fname) and os.stat(fname)[6] != 0:
			try:
	   			dbfile = open(fname)
	   		except IOError as ie:
	   			printData ='IOError occured\n'
	   			return printData
			datastr = dbfile.read()
			datastr = datastr.strip('\n').lower()
			maindb = datastr.split(';');
			for i in range(0,len(maindb)):
				maindb[i] =  maindb[i].split(',')
			for i in range(0,len(maindb)):
				t = {}
				tdbstr = ''
				for k in maindb[i]:
					temp = k.split('=')
					if len(temp)==2:
						t[temp[0]]=temp[1]
				if t.keys() == []:
					continue
				maindb[i] = t
			del(maindb[-1])
			dbfile.close()
		self.maindb= maindb
		if rnumber != 0:
			for x in gen_rand_data(rnumber,[],fname):
				if type(x) != dict:
					continue
				self.maindb.append(x)
		self.creattime = time.now()-start
		self.creattime = str(self.creattime.seconds+float(self.creattime.microseconds/1000000))
		return '\n'

	def insert(self,qstr):
		'''Insert a record into the database
		Syntax : field(1)=value(1),field(2)=value(2)...field(n)=value(n);'''
		self.instime=0
		start = time.now()
		qstr = qstr.strip()
		b = qstr.split(',')
		temp = ''
		fname = self.filename
		for x in b:
			d = {}
			c = x.split('=')
			print c
			if c[0].lower() == 'category':
				d['category'] = c[1]
				temp += 'category='+c[1]+','
				break
			if c[0].lower() == 'name':
				d['name'] = c[1]
				temp += 'name='+c[1]+','
				break
			if c[0].lower() == 'gender':
				d['gender'] = c[1]
				temp += 'gender='+c[1]+','
				break
			if c[0].lower() == 'year': 
				d['year'] = c[1]
				temp += 'year='+c[1]+','
				break
			if c[0].lower() == 'country':
				d['country'] = c[1]
				temp += 'country='+c[1]+','
				break
			if c[0].lower() == 'achievement':
				d['achievement'] = c[1]
				temp += 'achievement='+c[1]+','
				break
			else :
				print 'Error : No field %s in the database' %c[0]
				return False
			self.maindb.append(d)
		f = open(fname,'a')
		te = temp[:-1]+';'
		f.write(te)
		f.close()
		self.instime = time.now() - start
		self.instime = str(self.instime.seconds+float(self.instime.microseconds)/1000000)
		return True

	def project(self,proj,tresult):
		'''Returns projection onto specified 
		fields'''
		try:
			proj = proj.strip()
			if proj.lower() == 'all' or proj== '*':
				return tresult
			else:
				result = []
				projli = proj.split(',')
				for i in tresult:
					p = {}
					for j in projli: 
						p[j]=i.get(j,None)
					result.append(p)
				return result
		except:
			printData ='Wrong syntax field(s) not present in database\n'
			return printData

	def parseyear(self,query,n):
		'''Parse year attributes and returns True if 
		the specified operation on specified database row(dictionary)
		is True else returns False'''
		try:	
			if query.find('!=') != -1:
				query = query.split('!=')
				if query[1] != n.get(query[0],None):
					return True

			elif query.find('>=') != -1:
				query = query.split('>=')
				if query[1] <= n.get(query[0],None):
					return True
			elif query.find('<=') != -1:
				query = query.split('<=')
				if query[1] >= n.get(query[0],None):
					return True
			elif query.find('<') != -1:
				query = query.split('<')
				if query[1] > n.get(query[0],None):
					return True
			elif query.find('>') != -1:
				query = query.split('>')
				if query[1] < n.get(query[0],None):
					return True
			elif query.find('=') != -1:
				query = query.split('=')
				if query[1] == n.get(query[0],None):
					return True
			return False
		except : 
				printData = 'Error : Query %s is not in proper syntax'%query + '\n'
				return printData
				#sys.exit(0)

	def select(self,query):
		'''Select entries from the database.
		Syntax : <fields to be selected> where 
		condition(1) and/or condition(2) and/or 
		condition(3) ... condition(n).
		Here "and" has higher precedence than "or" '''
		start = time.now()
		query = query.lower()
		self.seltime=0
		try : 
			if query.find('where') == -1:
				if query.strip() == 'all' or query.strip() == '*':
					self.seltime = time.now() - start
					return self.maindb
				else:
					print 'Wrong syntax : no "where" keyword in query %s'%query 
					self.seltime = time.now() - start
					return []
			qlist = query.split('where')
			projstr = qlist[0]
			if qlist[1].strip(' ') == 'all' or qlist[1].strip() =='*':
				result = self.project(projstr,self.maindb)
				self.seltime = time.now() - start
				return result
			qlist = qlist[1].split(' or ')
			tresult = []		
			for j in qlist:
				temp = {}
				if j.find(' and ') == -1:
					j = j.strip()
					if j.find('year') != -1:
						for temp in self.maindb:
							if self.parseyear(j,temp):
								tresult.append(temp)

					elif j.find('!=') != -1:
						j = j.split('!=')
						for p in self.maindb:
							for k in p.keys():
								if j[0] == k:
									break
							if j[1] != p.get(j[0],None):
								tresult.append(p)
					else:
						j = j.split('=')
						for p in self.maindb:
							for k in p.keys():
								if j[0] == k:
									break
							if j[1] == p.get(j[0],None):
								tresult.append(p)

				else:
					andlist = j.split(' and ')
					for n in self.maindb:
						cnt = 0
						for ae in andlist:
							for be in andlist:
								ae = ae.strip()
								be = be.strip()
								if ae != be:
									cnt += 1
									if ae.find('year') != -1:
										abool = self.parseyear(ae,n)
									elif ae.find('!=') != -1 :
										al = ae.split('!=')
										abool = (al[1] != n.get(al[0],None))
									else:
										al = ae.split('=')							
										abool = (al[1] == n.get(al[0],None))

									if be.find('year') != -1:
											bbool = self.parseyear(be,n)

									elif be.find('!=') != -1 :
										bl = be.split('!=')
										bbool = (bl[1] != n.get(bl[0],None))
									else:
										bl = be.split('=')
										bbool = (bl[1] == n.get(bl[0],None))

									if abool and bbool:
										cnt -= 1 

						if cnt == 0:
							if n not in tresult:
								tresult.append(n)

					
			if tresult == []:
				return [] 
			result = self.project(projstr,tresult)
			self.seltime = time.now() - start
			self.seltime = str(self.seltime.seconds+float(self.seltime.microseconds)/1000000)
			return result
		except Exception as e :
			print 'Wrong Syntax :  Field(s) %s NOT present in  database '%query.split('where')[1]
			return []

	def update(self,qstr):
		'''Update an entry in the database
		Syntax : <field(s) to be updated> where condition(1) 
		and/or condition(2) and/or condition(3) ... condition(n)'''
		self.updtime=0
		fname = self.filename
		start = time.now()
		qstr = qstr.lower()
		qupdate = qstr.split('where')
		selected = self.select('all where '+qupdate[1])
		qupdate = qupdate[0].strip()
		qupdate = qupdate.split(',')
		for i in qupdate:
			j = i.split('=')
			p = {}
			if j[0].lower() == "name":
				for k in selected:
					p['name'] = j[1]
					p['category'] = k['category']
					p['country'] = k['country']
					p['year'] = k['year']
					p['gender'] = k['gender']
					p['achievement'] = k['achievement']
					del(self.maindb[self.maindb.index(k)])
					self.maindb.append(p)
			elif j[0].lower() == "year":
				for k in selected:
					p['year'] = j[1]
					p['category'] = k['category']
					p['country'] = k['country']
					p['name'] = k['name']
					p['gender'] = k['gender']
					p['achievement'] = k['achievement']
					del(self.maindb[self.maindb.index(k)])
					self.maindb.append(p)
			elif j[0].lower() == "gender":
				for k in selected:
					p['gender'] = j[1]
					p['category'] = k['category']
					p['country'] = k['country']
					p['year'] = k['year']
					p['name'] = k['name']
					p['achievement'] = k['achievement']
					del(self.maindb[self.maindb.index(k)])
					self.maindb.append(p)
			elif j[0].lower() == "category":
				for k in selected:
					p['category'] = j[1]			
					p['name'] = k['name']
					p['country'] = k['country']
					p['year'] = k['year']
					p['gender'] = k['gender']
					p['achievement'] = k['achievement']
					del(self.maindb[self.maindb.index(k)])
					self.maindb.append(p)
			elif j[0].lower() == "country":
				for k in selected:
					p['country'] = j[1]
					p['name'] = k['name']
					p['country'] = k['country']
					p['year'] = k['year']
					p['gender'] = k['gender']
					p['achievement'] = k['achievement']
					del(self.maindb[self.maindb.index(k)])
					self.maindb.append(p)
			elif j[0].lower() == 'achievement':
				for k in selected:
					p['achievement'] = j[1]
					p['country'] = k['country']
					p['name'] = k['name']
					p['country'] = k['country']
					p['year'] = k['year']
					p['gender'] = k['gender']
					del(self.maindb[self.maindb.index(k)])
					self.maindb.append(p)
			else :
				printData ='Error : Field %s not present in database'%j[0] + '\n'

			f = open(fname,"w")
			st = self.serialize()
			f.write(st)
			f.close()
			self.updtime = time.now() - start
			self.updtime = str(self.updtime.seconds+float(self.updtime.microseconds)/1000000)

	def delete(self,qdel):
		'''Delete an entry from the database
		Syntax : where condition(1) and/or condition(2) and/or 
		condition(3)... condition(n)'''
		self.deltime=0
		fname = self.filename
		start = time.now()
		self.dbstr = ''
		printData = ''
		try:
			tobedel = self.select('all '+qdel)
		except:
			printData+='No field %s in database' %qdel + '\n'
			return False
		try:
			for j in tobedel:
				printData+=  'Deleted \n'
				self.printdb([j])
				del(self.maindb[self.maindb.index(j)])
			st = self.serialize()
			f = open(fname,'w')
			f.write(st)
			f.close()
			self.deltime = time.now() -start
			self.deltime = str(self.deltime.seconds+float(self.deltime.microseconds)/1000000)
		except IOError as ie :
			printData+= 'IOError occuered'
			return False
		return True