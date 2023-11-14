# Find the factorial of a given number.

a=int(input("enter a number"))                        #iteration               #factorial*i
factorial=1                                             #i=1                     #1*1=1
if a<0:                                                 #i=2                     #1*2=2
    print("factorial does not exist")                   #i=3                     #2*3=3
elif a==0:
    print("the factorial 0 is 1")
else:
    for i in range(1,a+1):
        factorial=factorial*i
    print("the factorial of",a,"is",factorial)


# Find the factorial of a given number.
a=int(input("enter a number"))
factorial=1
for i in range(1,a+1):
    if a<0:
        print("factorial does not exist")
    elif a==0:
        print("the factorial 0 is 1")
    else:
        factorial=factorial*i
        print(factorial,end=",")