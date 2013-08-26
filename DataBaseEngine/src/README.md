Package wikidb
==============

##Module wikidb.wikidb


#####CLASSES
    Database
    
    class Database
     |  Methods defined here:
     |  
     |  create(self, fname, rnumber=0)
     |      Read from existing db file and create 
     |      the database.Also create database using 
     |      random entries.If the file you specify already exists 
     |      the new entries will be appended to the file and 
     |      original entries will be unchanged.If random entry generatation 
     |      option is not used then the database will be created using 
     |      the entries present in the file
     |  
     |  delete(self, fname, qdel)
     |      Delete an entry from the database
     |      Syntax : where condition(1) and/or condition(2) and/or 
     |      condition(3)... condition(n)
     |  
     |  insert(self, fname, qstr)
     |      Insert a record into the database
     |      Syntax : field(1)=value(1),field(2)=value(2)...field(n)=value(n);
     |  
     |  parseyear(self, query, n)
     |      Parse year attributes and returns True if 
     |      the specified operation on specified database row(dictionary)
     |      is True else returns False
     |  
     |  printdb(self, p=None)
     |      Print the database or the results
     |      in suitable format
     |  
     |  project(self, proj, tresult)

     |      Returns projection onto specified 
     |      fields
     |  
     |  select(self, query)
     |      Select entries from the database.
     |      Syntax : <fields to be selected> where 
     |      condition(1) and/or condition(2) and/or 
     |      condition(3) ... condition(n).
     |      Here "and" has higher precedence than "or"
     |  
     |  serialize(self)
     |      Convert the database object to
     |      strings for storing in file
     |  
     |  update(self, qstr, fname)
     |      Update an entry in the database
     |      Syntax : <field(s) to be updated> where condition(1) 
     |      and/or condition(2) and/or condition(3) ... condition(n)

#####FUNCTIONS
    gen_rand_data(datarange, database, fname='test.db')
        Generates random entries for the database
    
    id_generator(chars='abcdefghijklmnopqrstuvwxyz')
        Generates random strings of random length
    
    main()
        Parses command line arguments and creates
        the 'Database' object for performing operations 
        on it


##module wikidb.interactive

#####Fuctions

        interactive_menu()
        interactive menu generator for running 
        wikidb module
