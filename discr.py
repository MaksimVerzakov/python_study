class Property(object):
    def __init__(self, value):
        self.value = value   
     
    def __get__(self, instance, owner):
        return self.value

    def __set__(self, obj, value):
        if type(self.value) != type(value):
            raise TypeError
        self.value = value

class Image(object):
    height = Property(0)
    width = Property(0)
    path = Property('/tmp/')
    size = Property(0)

img = Image()
img.height = 340
print img.height
img.path = '/tmp/x00.jpeg'
print img.path
img.path = 320
