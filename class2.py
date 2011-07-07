class DictAttr(dict):
    def __getattr__(self, attr):
        try:
            return self[attr]
        except KeyError:
            raise AttributeError
        

x = DictAttr([('one', 1), ('two', 2), ('three', 3)])
print x
print x['three']
print x.get('one')
print x.get('one', 'missing')
print x.get('five', 'missing')
print x.one
#print x.five

class XDictAttr(DictAttr):
    def __getattr__ (self, attr):
        tmpstr = 'get_' + attr
        result = None
        if tmpstr in self.__class__.__dict__:
            result = self.__class__.__dict__[tmpstr](self)
        else:
            result = DictAttr.__getitem__(self, attr)
        return result
        
    def __getitem__(self, attr):
        tmpstr = 'get_' + attr
        if tmpstr in self.__class__.__dict__:
            result = self.__class__.__dict__[tmpstr](self)
        else:
            result = DictAttr.__getitem__(self, attr)
        return result
        
    def get(self, attr, d = None):
        tmpstr = 'get_' + attr
        if tmpstr in self.__class__.__dict__:
            result = self.__class__.__dict__[tmpstr](self)
        else:
            result = DictAttr.get(self, attr, d)
        return result
        
class X(XDictAttr):
    def get_foo(self):
        return 5
    def get_bar(self):
        return 12

x = X({'one': 1, 'two': 2, 'three': 3})
print x['one']
print x.three
print x.bar
print x['foo']
print x.get('foo', 'missing')
print x.get('bzz', 'missing')
