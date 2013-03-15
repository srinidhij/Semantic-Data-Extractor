from time import *
s = raw_input("Enter the base string : ")
x = raw_input("Enter the test input : ")
t1 = time()
s = s.replace(" ","")
x = x.replace(" ","")
ds = {}
dx = {}
flag = True
for q in s:
    if ds.has_key(q):
        ds[q]+=1
    else:
        ds[q]=1
for q in x:
    if dx.has_key(q):
        dx[q]+=1
    else:
        dx[q]=1
if len(ds)!=len(dx):
    flag = False
else:
    for k in ds.keys():
        try:
             if dx[k]!=ds[k]:
                 print k
                 flag = False
                 break
        except:
             flag = False
             break 
print ds,dx
if flag:
    print x," is an anagram of ",s
else:
    print x," is not an anagram of ",s
print 'Time taken = '+str(time()-t1)