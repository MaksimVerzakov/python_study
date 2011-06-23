#!/usr/env python
# show all attributes
print dir(1)
# show public attributes only
print [atr for atr in dir(1) if not atr.startswith('__')]

# show methods only
print [atr for atr in dir(1) if callable(getattr (1, atr))]

# Concatenation
a = (1,2,3)
b = (3,4,5)
print a+b

# Union
print a + tuple(x for x in a+b if x not in a)

# Dictionary
a = [1,2,3]
b = ['one', 'two', 'three']
d = dict(zip(a,b))
print d

# Dictionary
d = dict(map(None,a,b))

# Dictionary reverse
for d in d.keys:
    d[d[k]] = k
    d.pop(k)

# Stings1
s = u'Hello, world!'
s1 = s.encode('utf-8')
s2 = s.encode('cp1251')

# Strings2
s = 'Hello, world!'
su = unicode(s, 'cp1251')

