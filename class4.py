class IterableRegisterMetaClass(type):

    def __init__(cls, name, bases, dictionary):

        def counter(instance):
            instance.__class__._instances.append(instance)

        def decounter(instance):
            instance.__class__._instances.remove(instance)

        setattr(cls, '__init__', counter)
        setattr(cls, '__del__', decounter)
        setattr(cls, '_instances', [])

    def __iter__(cls):
        return iter(cls._instances)


class Reg:
    __metaclass__ = IterableRegisterMetaClass
    
x = Reg()
y = Reg()
z = Reg()
for i in Reg:
    print i
