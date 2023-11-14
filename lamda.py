# Anonomous function: sometimes we declare some funtion without any name
#syntax: lambda input:expresion
s=lambda n:2*n
print(s(2))


s=lambda n:2*n+n-n/n
print(s(2))


s=lambda a,b,c:a+b-c
print(s(10,20,30))


#type error : positional argument is missing "C"
s=lambda a,b,c:a+b-c
print(s(10,20))


# type error: here two positional arguments but were given three values
s=lambda a,b:a+b
print(s(10,20,30))


s=lambda a,b,c,d:a+b-c+d
print(s(10,20,30,d=10))


s=lambda a,b,c,d=10:a+b-c+d
print(s(10,20,30))


s=lambda a,b,c,d=10:a+b-c+d
print(s(10,20,30,d=20))



s=lambda a,b,c,d="i":a
print(s("s","u","j","I"))


def f1(n):
    return lambda a: a*n
b=f1(4)
print(b(10))


#In this 4=n,10=a and 3=n,11=a
def f1(n):
    return lambda a: a*n
b=f1(4)
c=f1(3)
print(b(10))
print(c(11))