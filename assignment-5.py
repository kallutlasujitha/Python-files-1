#Write a program to display all prime numbers within a range.
for i in range (2,50):
    out='Prime'
    for j in range(2,i):
        if i%j==0:
            out=("not prime")
            break
    if out=="Prime":
        print(i,end=",")

#Write a program to display all prime numbers within a range.
a=int(input("enter a number"))
b=int(input("enter a number"))
for i in range (a,b+1):
    out='Prime'
    for j in range(2,i):
        if i%j==0:
            out=("not prime")
            break
    if out=="Prime":
        print(i,end=",")

#Write a program to display all prime numbers within a range.
a=int(input("enter a number"))
b=int(input("enter a number"))
for i in range (a,b+1):
    if i>1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i,end=",")