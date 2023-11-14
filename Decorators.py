#Decorators:decor always going to take some input functions 
#and it will perform some action and it is going to produce output

def  a(f):
    def inner(n):
        if n=="rose":
            print('hi rose')
        else:
            f(n)
    return inner
@a
def b(n):
    print('hello',n)
b('tulip')
b('rose')
b('lilly')



def  a(f):
    def inner(n):
        if n=="tulip":
            print('hi tulip')
        else:
            f(n)
    return inner
@a
def b(n):
    print('hello',n)
b('tulip')
b('rose')
b('lilly')




def  a(f):
    def inner(n):
        if n==5:
            print(n,'odd number')
        else:
            f(n)
    return inner
@a
def b(n):
    print('number is',n)
b(55)
b(555)
b(5555)



def  a(f):
    def inner(n):
        if n==5 or n>=5:
            print(n,' is divisible by 11')
        else:
            f(n)
    return inner
@a
def b(n):
    print('number is',n)
b(55)
b(555)
b(5555)



def  a(f):
    def inner(n):
        if n=="rose":
            print('hi rose')
        else:
            f(n)
    return inner
@a
def b(n):
    print('hello',n)
b('tulip')
b('lilly')
b('rose')
@a
def c(n):
    print('hey',n)
c('hai')
c('man')
c('hai')