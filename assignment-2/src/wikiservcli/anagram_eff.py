from time import time
from re import findall
from collections import defaultdict

s = raw_input("Enter the base string : ")
x = raw_input("Enter the test input : ")
def isAnagram(s,x):
    '''Checks if two string are anagrams 
	of each other efficiently'''
    if len(s) != len(x):
        return False
    s = ''.join(findall('[a-z]+',s.lower()))
    x = ''.join(findall('[a-z]+',x.lower()))
    ds = defaultdict(lambda: 1)
    dx = defaultdict(lambda: 1)
    flag = True
    for q in s: 
        ds[q]+=1
    for q in x:
         dx[q]+=1
    for k in ds.keys():
         try:
            if dx[k]!=ds[k]:
                print k
                flag = False
                break
        except:
            flag = False
            break
    return flag 
t1 = time()
a = isAnagram(s,x)
t2 = time()
if a:
    print x," is an anagram of ",s
else:
    print x," is not an anagram of ",s
print 'Time taken = '+str(t2-t1)
