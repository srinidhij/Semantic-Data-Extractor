from time import *
from re import findall
s = raw_input("Enter the base string : ")
x = raw_input("Enter the test input : ")
def isAnagram(s,x):
	'''Checks if two strings are anagrams of 
	each other via brute force method'''
	if len(x) != len(s):
	return False
	s = ''.join(findall('[a-z]+',s.lower()))
	x = ''.join(findall('[a-z]+',x.lower()))
	cnt = 0
	for i in x:
		for j in s:
			if i==j:
				cnt += 1
	if cnt==len(s):
		return True
	return False
t1 = time()
print isAnagram(s,x)
print 'Time taken = '+str(time()-t1)
