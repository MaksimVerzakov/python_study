def f(*args):
    res = 0;
    for a in args:
        if hasattr(a,'__len__'):
            res += f(*a)
        else:
            res += a
    return res

print f(2, (2,3,4))
