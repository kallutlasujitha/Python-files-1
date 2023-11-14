def  a(f):
    def inner(n):
            print(n,' first decor execution')
            f(n)
    return inner
def  b(f):
    def inner(n):
            print(n,'second decor execution')
            f(n)
    return inner
@a
@b
def c(n):
    print('hello',n, 'how are u')
c('rose')




def  a(f):
    def inner():
            x=f()
            return x*x
    return inner
def  b(f):
    def inner():
            x=f()
            return 2*x
    return inner
@a
@b
def c():
    return 20
print(c())



# def  a(f):
#     def inner(n):
#             x=f()
#             return x*x
#     return inner
# def  b(f):
#     def inner(n):
#             x=f()
#             return 2*x
#     return inner
# @a
# @b
# def c(n):
#     return 20
# print(c(10))