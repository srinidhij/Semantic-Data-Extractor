from time import *
s = raw_input("Enter the base string : ")
x = raw_input("Enter the test input : ")
t1 = time()
s = [r for r in s.replace(" ","")]
x = [r for r in x.replace(" ","")]
print x,s
for q in s:
	try:
		i = x.index(q)
		del x[i]
	except:
		break
if not x:
    print x," is an anagram of ",s
else:
    print x," is not an anagram of ",s
print 'Time taken = '+str(time()-t1)