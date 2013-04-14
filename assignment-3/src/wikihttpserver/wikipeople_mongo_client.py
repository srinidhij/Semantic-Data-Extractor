from pymongo import *
import webbrowser
client = MongoClient('localhost',27017)
db = client.WikiPeopleDatabase
wikipeople = db.WikiPeopleDatabase
name = True
category = True
achievement = True
year = True
country = True
gender = True
printData = '<html><title>WikiPeopleDatabase</title><body><table border=1><tr>'
if name:
	printData+='<th>Name</th>'
if category:
	printData+='<th>Category</th>'
if year:
	printData+='<th>Year</th>'
if country:
	printData+='<th>Country</th>'
if gender:
	printData+='<th>Gender</th>'
if achievement:
	printData+='<th>Achievement</th>'
printData+='</tr>'
temp = wikipeople.find({"year":"2014"}, {'_id': False})
for result_object in temp:
	printData+= '<tr>'
	for key,value in dict(result_object).items():
		printData+= '<td>'+value+'</td>'
	printData+=  '</tr>'
printData+= '</table></body></html>'
f = open("gen.html",'w')
f.write(printData)
f.close()
webbrowser.open("gen.html") 