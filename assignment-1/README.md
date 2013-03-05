#Assignment 1 


###Usage
          usage: wikidb.py [-h] [-i --insert] [-u --update] [-d --delete]
                 [-f --filename] [-g --generate] [-s --select] [--interactive]

          optional arguments:
            -h, --help     show this help message and exit
            -i --insert    Insert entries into the database
            -u --update    Update the entries in the database
            -d --delete    Delete an entry in database
            -f --filename  Filename which contains the database
            -g --generate  Generates the random entries for the database
            -s --select    Select particular entries from database
            --interactive  Run in interactive mode
            

#####Create:
           Read from existing db file and create 
           the database.Also create database using 
           random entries.If the file you specify already exists 
           the new entries will be appended to the file and 
           original entries will be unchanged.If random entry generatation 
           option is not used then the database will be created using 
           the entries present in the file

#####Select:
           Select entries from the database.
           Syntax : <fields to be selected> where 
           condition(1) and/or condition(2) and/or 
           condition(3) ... condition(n).
           For integer fields condition can be <, <=, >, >=, = ,!=
           for non-integer fields condition can only be != or =
           Here "and" has higher precedence than "or"
           Eg :   'all where country=india and category!=physics or year>2005'
           
#####Insert:
           Insert a record into the database
           Syntax : field(1)=value(1),field(2)=value(2)...field(n)=value(n);
           Eg : 'name=pqr lmn,category=physics,year=2013,achievement=asdfasdf,country=india'
  
#####Update:
           Update an entry in the database
           Syntax : <field(s) to be updated> where condition(1) 
           and/or condition(2) and/or condition(3) ... condition(n)
           Eg : 'name=abcd efgh,category=economics where name=pqr lmn'
        
#####Delete:
           Delete an entry from the database
           Syntax : where condition(1) and/or condition(2) and/or 
           condition(3)... condition(n)
           Eg : 'category=physics and gender=m'
           
