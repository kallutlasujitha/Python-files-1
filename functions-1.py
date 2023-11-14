# def f1():
#     return
# f1()



def fname(a,b):
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)
fname(10,20)
fname(2,3)


def fname(a,b):
    print(a+b)
    return 10  #we are not returning the value, if you write anything in return it's not printed
fname(11,20)


def fname(a,b):
    print(a,"are beautiful and pretty",b)
fname("roses","also")


def fname(a,b):
    return(a,"are beautiful and pretty",b)
c=fname("roses","also")
print(c)


def fname(a,b,c,d):
    print(a,": rose",b,": lilly",c,": marie",d,": tulip")
c=fname(1,2,3,4)
print(c)



