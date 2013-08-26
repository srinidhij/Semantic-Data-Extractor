from pymongo import *
from time import time
import datetime
import sys

def errorMongoDB(e):
    data = "<html><title>WikiPeopleDatabase</title><body>"+"The following exception occurred while connecting to the database : "+str(e)+"</body></html>"
    return data

class QueryDB:
    def processQuery(self,form):
        try:
            client = MongoClient('localhost',27017)
            db = client.WikiPeopleDatabase
            wikipeople = db.WikiPeopleDatabase
        except Exception as e:
            return errorMongoDB(sys.exc_info())
        fields = dict(form)
        temp = {}
        for key in fields.keys():
            temp[key] = form.getlist(key)[0]

        try:
            query = temp['query'].strip()
        except:
            query = ''
        name = year = achievement = country = category = False           
        toBeDisplayed = {'_id':False}
        styles = r'''  <style>
#wikipeople td, #wikipeople th 
{
font-size:1em;
border:1px solid #5858FA;
padding:3px 7px 2px 7px;
}
#wikipeople th 
{
font-size:1.1em;
text-align:left;
padding-top:5px;
padding-bottom:4px;
background-color:#08088A;
color:#ffffff;
}
#wikipeople tr.alt td 
{
color:#000000;
background-color:#5858FA;
}
</style>
            '''
	style2 = '<link rel="stylesheet" href="foundation.css">'
        printData = '<html><head><title>WikiPeopleDatabase</title>'+style2
        printData+='''
        <script type="text/javascript">
        function post_to_url(buttonId) {
            var form = document.createElement("form");
            form.setAttribute("method", "post");
            form.setAttribute("action", "http://localhost:8008/servf.py");
            var nobel = document.getElementById(buttonId).value;
            var hiddenField = document.createElement("input");
            hiddenField.setAttribute("type", "hidden");
            hiddenField.setAttribute("name", "query");
            hiddenField.setAttribute("value", nobel);
            form.appendChild(hiddenField);
            document.body.appendChild(form);
            form.submit();
        }
</script></head><body><h1 align="center">Query Results</h1><div class="row"><div class="twelve-columns-centered"><table align="center" border=1 id="wikipeople"><tbody><tr>
        '''
        try:
            if temp['displaycategory']=='on':
                printData+='<th>Category</th>'
                category = True
        except:
            toBeDisplayed['category'] = False
        try:
            if temp['displayname']=='on':
                printData+='<th>Name</th>'
                name = True
        except:
            toBeDisplayed['name'] = False
        try:
            if temp['displayyear']=='on':
                printData+='<th>Year</th>'
                year = True
        except:
            toBeDisplayed['year'] = False
        try:
            if temp['displaycountry']=='on':
                printData+='<th>Country</th>'
                country = True
        except:
            toBeDisplayed['country'] = False
        try:
            if temp['displayachievement']=='on':
                printData+='<th>Achievement</th>'
                achievement = True
        except:
            toBeDisplayed['achievement'] = False  
        printData+='</tr>'
        dataname = datayear = datacategory = datacountry = dataachievement  = ''
        toBeProcessed = {}
        try:
            if temp['category']:
                toBeProcessed['category'] = temp['category']
                datacategory = temp['category']                    
        except:
            datacategory = ''
        try:
            if temp['name']:
                toBeProcessed['name'] = temp['name']
                dataname = temp['name']                    
        except:
            dataname = ''
        try:
            if temp['country']:
                toBeProcessed['country'] = temp['country']
                datacountry = temp['country']                    
        except:
            datacountry = ''
        try:
            if temp['achievement']:
                toBeProcessed['achievement'] = temp['achievement']
                dataachievement = temp['achievement']                    
        except:
            dataachievement = ''
        try:
            if temp['year']:
                toBeProcessed['year'] = temp['year']
                datayear = temp['year']                    
        except:
            datayear = ''
        dataIn = {'name':[],'year':[],'country':[],'achievement':[],'category':[]}
        dataNotIn = {'name':[],'year':[],'country':[],'achievement':[],'category':[]}
        
        if datacategory:
            if datacategory.split('=')[0] == '':
                dataIn['category'] = datacategory.split('=')[1].split(',')
            elif datacategory.split('!=')[0] == '':
                dataNotIn['category'] = datacategory.split('!=')[1].split(',')
        if dataname:
            if dataname.split('=')[0] == '':
                dataIn['name'] = dataname.split('=')[1].split(',')
            elif dataname.split('!=')[0] == '':
                dataNotIn['name'] = dataname.split('!=')[1].split(',')
        if dataachievement:
            if dataachievement.split('=')[0] == '':
                dataIn['achievement'] = dataachievement.split('=')[1].split(',')
            elif dataachievement.split('!=')[0] == '':
                dataNotIn['achievement'] = dataachievement.split('!=')[1].split(',')
        if datacountry:
            if datacountry.split('=')[0] == '':
                dataIn['country'] = datacountry.split('=')[1].split(',')
            elif datacountry.split('!=')[0] == '':
                dataNotIn['country'] = datacountry.split('!=')[1].split(',')
        if datayear:
            if datayear.split('=')[0] == '':
                dataIn['year'] = datayear.split('=')[1].split(',')
            elif datayear.split('!=')[0] == '':
                dataNotIn['year'] = datayear.split('!=')[1].split(',')
        for key,value in dataIn.items():
            if value==[]:
                del dataIn[key]
        for key,value in dataNotIn.items():
            if value==[]:
                del dataNotIn[key] 
            
        temp = [x.split(" and ") for x in query.split(" or ")]
        andAttrb = [x for x in temp if len(x)>1]
        orAttrb = [x for x in temp if x not in andAttrb]

        fQuery = []
        for l in andAttrb:
            tQuery = []
            for attr in l:
                for key,val in dataIn.items():
                    if key==attr:
                        tQuery.append({key:{'$in':val}})
                for key,val in dataNotIn.items():
                    if key==attr:
                        tQuery.append({key:{'$nin':val}})
                #print 'tQuery ',tQuery
            fQuery.append({'$and':tQuery})
        
        for l in orAttrb:
            for attr in l:
                for key,val in dataIn.items():
                    if key==attr:
                        fQuery.append({key:{'$in':val}})
                for key,val in dataNotIn.items():
                    if key==attr:
                        fQuery.append({key:{'$nin':val}})
                #print 'fQuery ',fQuery
        fname = "../../logs/log"+str(datetime.date.today())+".txt"
        f = open(fname,"a")
        print 'Final Query: ',fQuery
        f.write('Query Executed '+str(fQuery)+'\n')
        f.close()
        print orAttrb,andAttrb
        try:
            t1 = time()
            if orAttrb==[['']] and not andAttrb:
                temp = wikipeople.find({},toBeDisplayed)
                t2 = time() - t1
                count =  wikipeople.find({}).count()
            else:
                temp = wikipeople.find({ '$or': fQuery},toBeDisplayed)
                t2 = time() - t1
                count =  wikipeople.find({ '$or': fQuery}).count()
        except Exception as e:
	    f = open()
            return errorMongoDB("Invalid Query")
        buttonId = 0
        for result_object in temp:
            #print result_object
            buttonId+=1
            printData+= '<tr>'
            r = dict(result_object)
            #print r
            if category==True:
                try:
                    printData+= '<td>'+r['category']+'</td>'
                except:
                    printData+= '<td>'+'Empty'+'</td>'
            if name==True:
                try:
                    printData+= '<td><input class="but" type="button" id="'+str(buttonId)+'" name="query" onclick="post_to_url(this.id)" value="'+r['name']+'" style="border-style:none;background-color:#eeeeee;" /></td>'
                except:
                    printData+= '<td>'+'Empty'+'</td>'
            if year==True:
                try:
                    printData+= '<td>'+r['year']+'</td>'
                except:
                    printData+= '<td>'+'Empty'+'</td>'
            if country==True:
                try:
                    printData+= '<td>'+r['country']+'</td>'
                except:
                    printData+= '<td>'+'Empty'+'</td>'
            if achievement==True:
                try:
                    printData+= '<td>'+r['achievement']+'</td>'
                except:
                    printData+= '<td>'+'Empty'+'</td>'

            printData+=  '</tr>'
        printData+= '</tbody></table></div></div></br><h3 align="center">'+str(count)+" results fetched out of "+str(wikipeople.count())+" entries in "+str(t2)+" seconds"+'</h3>'
        printData+= '</body></html>'
        return printData
