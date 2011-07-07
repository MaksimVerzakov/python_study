class Observable:

    def __init__(self, **kwargs):
        self.__dict__ = kwargs

    def printattr(self):
        tmp = ()
        for attr in self.__dict__:
            if not attr.startswith('_'):
                tmpstr = '%s = %s' % (attr, self.__dict__[attr])
                tmp = tmp +(tmpstr,)
        return tmp

    def __str__(self):
        return '%s %s' % (self.__class__.__name__, self.printattr())
        

if __name__ == '__main__':
    class X(Observable):
        pass
        
    x = X(foo=1, bar=5, _bazz=12, name='Amok', props=('One', 'two'))
    print x
    print x.foo
    print x.name
    print x._bazz
