def def1(a,b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    print("After Swapping a =",a,"b =",b)
def1(1,2)
def def2(a,b):
    a = (a & b) + (a | b)
    b = a + (~b) + 1
    a = a+(~b) + 1
    print("After Swapping a =",a,"b =",b)
def1(3,4)
def2(1,2)