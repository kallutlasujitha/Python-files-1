def fact(a):
    if a==0:
        r=1
    else:
        r=a*fact(a-1)
        return r
fact(4)


def f1(n):
    a=0
    b=1
    if n==1:
        print(a)
    else:
        print(a,end=',')
        print(b,end=',')
        for i in range(2,n):
            c=a+b
            a=b
            b=c
            print(c,end=',')
f1(10)