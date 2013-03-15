import sys
try:
	from wikidb import Database
except:
	'Print module wikidb not found'
	sys.exit(1)
def interactive_menu():
	'''interactive menu generator for running 
	wikidb module '''
	db = None
	print 'Welcome to Database Server'
	while True:
		prompt = 'wikidb>'
		print '#'*75
		print ' Choose an option : '
		print ' 1. Create database '
		print ' 2. Select entries from database '
		print ' 3. Insert an entry into the database '
		print ' 4. Update an entry in the database '
		print ' 5. Delete an entry in the database '
		print ' 6. Exit '
		print '#'*75
		ch = raw_input()
		try:
			if int(ch) == 1:
				db =Database()
				print 'If the file you specify already exists the new entries will be\n \
appended to the file and original entries will be unchanged'
				fname = raw_input(' Enter the file name : \n%s '%prompt)
				rnd = raw_input(' Do you want to generate random entries (Y/n) :\n%s '%prompt)
				if rnd.lower() == 'y':
					nentries = int(raw_input(' Enter number of entries :\n%s '%prompt))
					db.create(fname,nentries)
				else : 
					print 'Creating database from entries already present in file %s'%fname
				if fname is None:
					print 'Error Please Enter again'
					continue
				db = Database()
				db.create(fname)
				print ' Database Created in %s s'%db.creattime
			elif int(ch) == 2:
				if db is None:
					print ' Please create database first'
					continue
				print '''Syntax : <fields to be selected> where 
	condition(1) and/or condition(2) and/or 
	condition(3) ... condition(n).
	Here "and" has higher precedence than "or" '''
				query = raw_input(' Enter select query : \n%s'%prompt)
				a = db.select(query)
				db.printdb(a)
				print 'in %s s '%db.seltime
			elif int(ch) == 3:
				if db is None:
					print ' Please create database first'
					continue
				query = raw_input(' Enter record to be inserted:\n%s'%prompt)
				db.insert(fname,query)
				print '%s Inserted '%prompt,query, ' Successfully in %s s'%db.instime
			elif int(ch) == 4:
				if db is None:
					print 'Please create database first'
					continue
				print '''Update an entry in the database
	Syntax : <field(s) to be updated> where condition(1) 
	and/or condition(2) and/or condition(3) ... condition(n)'''
				query = raw_input(' Enter update query : \n%s'%prompt)
				db.update(query)
				print 'Updated all entries where ',query, ' Successfully in %s s '%db.updtime
			elif int(ch) == 5:
				if db is None:
					print ' Please create database first'
					continue
				print '''Delete an entry from the database
	Syntax : where condition(1) and/or condition(2) and/or 
	condition(3)... condition(n)'''
				query = raw_input(' Enter delete query : \n%s'%prompt)
				db.delete(fname,query)
				print 'Deleted all entries where ',query, ' Successfully in %s s '%db.deltime
			elif int(ch) == 6:
				print  'Bye'
				return
		except :
			print '%s wrong syntax'%prompt