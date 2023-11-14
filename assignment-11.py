# Find the sum of the series upto n terms.

#l=[1,2,3,4,5]
n=int(input("enter a number"))
x=int(input("enter a number"))
sum=1
for i in range(2,n+1):
    sum=sum+((x**i)/i)
print(sum,2)
