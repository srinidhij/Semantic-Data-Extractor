from time import time
from re import findall
x = raw_input('Enter string 1 : ')
y = raw_input("Enter string 2 : ")
def isAnagram(m,n):
	mstr = ''.join(findall('[a-z]+',m.lower()))
	nstr = ''.join(findall('[a-z]+',n.lower()))
	ml = list(mstr)
	nl = list(nstr)
	return ml.sort() == nl.sort()
t= time()
print isAnagram(x,y)
e=time()
print 'timetaken = '+str(e-t)
