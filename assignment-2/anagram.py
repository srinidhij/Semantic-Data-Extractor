def isAnagram(m,n):
	mstr = ''.join(m.split())
	nstr = ''.join(n.split())
	mstr = ''.join(sorted(list(mstr)))
	nstr = ''.join(sorted(list(nstr)))
	return mstr == nstr
print isAnagram('mother in law','woman hitler')
