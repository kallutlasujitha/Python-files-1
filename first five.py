
def f1(a,b):
    return a+b
c=f1(10,20)
print(c)


def f1(a):
    if a%2==0:
        return (True,"because its even")
    else:
        return (False,"because its odd")
f1(9)
print(f1(9))



def f1(a):
    if a>0:
        print(a,"is positive number")

    else:
        print(a,"is negative number")
f1(-10)



def f1(a):
    if (0<=a<=9):
        print("given character is number")
    else:
        print("given character is not a number")
f1(1)




def f1(p):
    if('a'<=p<='z'):
        print('lower case')
    else:
        print('upper case')
f1('b')



def f1(p):
    if('A'<=p<='Z' or 'a'<=p<='z' or '0'<=p<='9'):
        print(p,'not a special character')
    else:
        print(p,'special character')
f1('*')



def f1(*a):
    if len(a)%2==1:
        b=len(a)//2
        print(a[b])
        print('the list has mid value')
    else:
        print('the list has no mid value')
f1(0,1,2,10,4.5,3+5j,'hello')






