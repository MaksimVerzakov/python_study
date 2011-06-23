def chain(*iterators):
    for it in iterators:
        for i in it:
            yield i

i1 = iter([1,2,3])
i2 = iter ([4,5,6])
c = chain(i1,i2)
print c.next()
print c.next()
print c.next()
print c.next()
print c.next()
print c.next()
