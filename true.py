import dis
def add(a,b):
    return a+b

dis.dis(add)
def mul(a,b):
    return a*b
dis.dis(mul)
def printw(a):
    print(a)
    return None
dis.dis(printw)

