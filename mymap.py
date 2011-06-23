def mymap(func,args):
    if hasattr(func,'__len__'):
        return [[f(arg) for arg in args] for f in func]
    else:
        return [func(arg) for arg in args]
print mymap(add5, (1,2,3))
