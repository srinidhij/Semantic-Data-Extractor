#!/usr/bin/python
from BeautifulSoup import BeautifulSoup

class HTMLParser:
	def __init__(self,html=None):
		self.html = html.replace('\xc3','o')
		self.soup = BeautifulSoup(html)
		self.table = self.soup.findAll('table')[1]	
		self.p = self.table.findAll('tr')

	def performcleanup(self,data):
		for i in range(0,len(data)):
			if type(data[i]['country']) == list:
				data[i]['country'] = data[i]['country'][0]
			data[i]['achievement'] = data[i]['achievement'].replace('"','')
			pos = data[i]['achievement'].find('<sup')
			if (pos != -1):
				data[i]['achievement'] = data[i]['achievement'][:pos]
		return data
	def convert(self,data):
		for i in range(len(data)):
			for key in data[i].keys():
				a = data[i][key]
				if type(a) == int:
					continue 
				st = ''
				for p in a:
					try:
						st += str(p)
					except:
						pass
				data[i][key] = st
		return data

	def parse(self,category):
		j = 0
		data = []
		p = self.p
		while j < len(p):
			t = dict()
			tdele = p[j].findAll('td')
			try:
				if tdele[0].has_key('rowspan'):

					rspan = int(tdele[0]['rowspan']) 
					year = int(tdele[0].contents[0])
					
					t['year'] = year
					if tdele[2].a:
						t['name'] = tdele[2].a.contents[0]
					else:
						t['name'] = tdele[2].contents
					if tdele[3].a:
						t['country'] = tdele[3].a.contents[0]
					else:
						t['country'] = tdele[3].contents
					achstr = ''
					ach = tdele[4].contents
					for temp in ach:
						if str(type(temp)) == "<class 'BeautifulSoup.Tag'>" and str(type(temp.contents[0])) != "<class 'BeautifulSoup.Tag'>":
							achstr += temp.contents[0]
						else:
							achstr += str(temp)
					t['achievement'] = achstr
					if category.lower() == 'literature':
						achstr += ' work : '
						ach = tdele[5].contents
						for temp in ach:
							if str(type(temp)) == "<class 'BeautifulSoup.Tag'>" and str(type(temp.contents[0])) != "<class 'BeautifulSoup.Tag'>":
								achstr += temp.contents[0]
							else:
								achstr += str(temp)
					t['achievement'] = achstr
					t['category'] = category
					data.append(t)
					
					while rspan >= 2:
						t = dict()
						t['year'] = year
						j += 1
						rspan -= 1
						tdele = p[j].findAll('td')
						if tdele[1].a:
							t['name'] = tdele[1].a.contents[0]
						else:
							t['name'] = tdele[1].contents
						if tdele[2].a:
							t['country'] = tdele[2].a.contents[0]
						else:
							t['country'] = tdele[2].contents
						try:
							ach = tdele[3].contents
							achstr = ''
							for temp in ach:
								if str(type(temp)) == "<class 'BeautifulSoup.Tag'>" and str(type(temp.contents[0])) != "<class 'BeautifulSoup.Tag'>":
									achstr += temp.contents[0]
								else:
									achstr += str(temp)
							if category.lower() == 'literature':
								achstr += ' work : '
								ach = tdele[4].contents
								for temp in ach:
									if str(type(temp)) == "<class 'BeautifulSoup.Tag'>" and str(type(temp.contents[0])) != "<class 'BeautifulSoup.Tag'>":
										achstr += temp.contents[0]
									else:
										achstr += str(temp)
							t['achievement'] = achstr
						except :
							t['achievement'] = achstr
						t['category'] = category
						data.append(t)
				else:
					year = int(tdele[0].contents[0])
					t['year'] = year
					if tdele[2].a:
						t['name'] = tdele[2].a.contents[0]
					else:
						t['name'] = tdele[2].contents
					if tdele[3].a:
						t['country'] = tdele[3].a.contents[0]
					else:
						t['country'] = tdele[3].contents
					achstr = ''
					ach = tdele[4].contents
					for temp in ach:
						if str(type(temp)) == "<class 'BeautifulSoup.Tag'>" and str(type(temp.contents[0])) != "<class 'BeautifulSoup.Tag'>":
							achstr += temp.contents[0]
						else:
							achstr += str(temp)
					t['achievement'] = achstr
					if category.lower() == 'literature':
						achstr += ' work : '
						ach = tdele[5].contents
						for temp in ach:
							if str(type(temp)) == "<class 'BeautifulSoup.Tag'>" and str(type(temp.contents[0])) != "<class 'BeautifulSoup.Tag'>":
								achstr += temp.contents[0]
							else:
								achstr += str(temp)
					t['achievement'] = achstr
					t['category'] = category
					data.append(t)
			except:
				pass
			j += 1
		data = self.performcleanup(data)
		data = self.convert(data)
		return data


def main():
	i = 0
	parser = HTMLParser(''.join(open('sample.html').readlines()))
	data = parser.parse('physics')
	for dat in data:
		print dat
		print '\n\n'
if __name__ == '__main__':
	main()
