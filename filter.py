#syntax= filter (function,sequence)
def f1(a):
    if a%2==0:
        return False
    else:
        return True
l=[10,20,30,40,50,70,19]
l1=list(filter(f1,l))
print(l1)


def f1(a):
    if a%2==0:
        return True
    else:
        return False
l=[10,20,30,40,50,70,19]
l1=list(filter(f1,l))
print(l1)


l=[1,10,20,3,30,40,5,50,60,7,70,80,9,90]
print(list(filter(lambda x:x%2==1,l)))


l=[10,20,30,40,50,60,7,8]
l1=(list(filter(lambda x:x%2==0,l)))
print(l1)



a=[10,20,30,40]
def f1(x):
    if x<18:
       return False
    else:
        return True
b=filter(f1,a)
for x in b:
    print(x)

    