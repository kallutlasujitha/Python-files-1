#ZERO DIVISION ERROR:

# try:
#     a=10
#     b=0
#     c=a/b
#     print(c)
# except ZeroDivisionError:
#     print("divided by zero is not possible")


# try:
#     a=int(input("enter a number"))
#     b=int(input("enter a number"))
#     c=a/b
#     print(c)
# except ZeroDivisionError:
#     print("divided by zero is not possible")


# try:
#     a=int(input("enter a number"))
#     b=10/a
#     print(b)
# except ZeroDivisionError:
#     print("divided by zero is not possible")


# def division(a,b):
#     try:
#         c=a/b
#         print(c)
#     except ZeroDivisionError:
#         print("divided by zero is not possible")
# a=int(input("enter a number"))
# b=int(input("enter a number"))
# division(a,b)


#VALUE ERROR:

# try:
#     a=input("enter a number")
#     b=int(a)
#     print(b)
# except TypeError:
#     print("hello")
# except ValueError:
#     print("hi")


# try:
#     a=input("enter a number")
#     b=int(a)
#     print(b)
# except BaseException:
#     print("hello")


# def value(a):
#     try:
#         # a=(input("enter a number"))
#         b=int(a)
#         print(b)
#     except ValueError:
#         print("hello")
# a=(input("enter a number"))
# value(a)


#TYPE ERROR:

# try:
#     a="ss"
      #b=2
#     if a%b==0:
#         print("hello")
#     else:
#         print("hai")
# except TypeError:
#     print("hi")

# def type(a,b):
#     try:
#         if a%b==0:
#             print("hello")
#     except TypeError:
#         print("its a type error")
# a=input("enter a data")
# b=int(input("enter a data"))
# type(a,b)


#INDEX ERROR:
# try:
#     a=int(input("enter a number"))
#     b=int(input('enter a number'))
#     c=a[b]
#     print(c)
# except IndexError:
#     print('hello')




# def division(a,b):
#     try:
#         c=a/b
#         print(c)
#     except ArithmeticError:
#         print("divided by zero is not possible")
# a=int(input("enter a number"))
# b=int(input("enter a number"))
# division(a,b)

