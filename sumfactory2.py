def addition_range(*range_):
    def addlist(x):
        def add(int):
            return int + x
        return add
    return [addlist(a) for a in xrange(*range_)]

add5 = addition_range(0,5)
for f in add5:
    print f(3)
