def addition(x):
    def add(int):
		return int + x
    return add

add5 = addition(5)
print add5(6)

def additionl(x):
    return lambda int: x + int
  
add5 = additionl(5)
print add5(6)

    


