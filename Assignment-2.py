#ASSIGNMENT-2.1
a=[10,20,30,40,50,60,70,80,90]
b=int(input("enter a number"))
index=-1
for i in range (len(a)):
    if a[i]==b:
        index=i
        break
if index !=-1:
    print(f"{b} is available and first occurrence is at index:{index}")
else:
    print(f"{b} is not present in the list")


#ASSIGNMENT-2.2
a=list(range(1,51))
print(a,end=" ")
for n in a :
    n = int(input('enter a number'))
    if n == 0:
        break
    if 1<=n<=50:
        if n in a:
            a.remove(n)
            print('deleted')
        else:
             print('out of range')
print(a)