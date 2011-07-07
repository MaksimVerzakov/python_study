class Reg():
    reglist = []
    def __init__(self):
        Reg.reglist.append(self.__class__) 
        Reg.offset = 0
               
    def __rerp__(self):
        return self
        
    def __iter__(self):
        return self
         
    def next(self):
        if self.offset >= len(Reg.reglist):
            raise StopIteration
        result = Reg.reglist[self.offset]
        self.offset += 1
        return result
           
    def __del__(self):
        Reg.reglist.remove(self.__class__)
            
            
if __name__ == '__main__':
    x = Reg()
    y = Reg()
    print x, y
    print Reg.reglist
    y = 2
    print Reg.reglist
    for i in Reg():
        print i
