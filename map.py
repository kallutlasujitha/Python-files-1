#syntax: map(function,iterables)

l=[1,10,20,3,30,40,5,50,60,7,70,80,9,90]
print(list(map(lambda x:x%2==1,l)))


#if you give like this , we will get output as a generator
l=[1,10,20,3,30,40,5,50,60,7,70,80,9,90]
print(map(lambda x:x%2==1,l))


def f1(a):
    return len(a)
x=map(f1,('roses','are','red colour'))
print(list(x))


def f1(a,b):
    return a+b
x=map(f1,('roses','are','red'),(' lilly,s',' in',' and white colour'))
print(list(x))


def f1(a):
    return a+a
x=(1,2,3,4)
y=map(f1,x)
print(list(y))