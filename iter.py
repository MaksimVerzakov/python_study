def cycle(iterator):
    saved = []
    for i in iterator:        
        yield i
        saved.append(i)
    while saved:
        for i in saved:
            yield i
       
i = iter([1,2,3])
c = cycle(i)
print c.next()
print c.next()
print c.next()
print c.next()

