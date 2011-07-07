def my_set_attr(self, attr, value):
    if attr in self.__class__.__dict__:
        data = self.__class__.__dict__[attr]
        if type(data) == type(value):
            self.__dict__[attr] = value
        else:
            raise TypeError
    else:
        self.__dict__[attr] = value
    

class Meta(type):
    def __new__(meta, classsname, supers, classdict):
        classdict['__setattr__'] = my_set_attr
        return type.__new__(meta, classsname, supers, classdict)

class Image():
    height = 0
    width = 0
    path = '/tmp'
    size = 0

    __metaclass__ = Meta

if __name__ == '__main__':
    im = Image()
    print im.height
    im.height = 12
    print im.height
    print im.size
    im.size = 'sd'
    print im.size

    
