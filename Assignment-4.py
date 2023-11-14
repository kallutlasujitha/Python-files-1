#pro to take a tuple of numbers from keyboard and print Sum,average
t=(10,20,30,40,50)
sum=0
for i in t:
    sum+=i
average=sum/len(t)
print("sum:",sum)
print("average",average)


#pro to take a tuple of numbers from keyboard and print Sum,average
x=input("enter a numbers")
y=x.split()
#sum =sum(x)
sum=0
for i in y:
    sum+=i
average=sum/len(x)
print("sum:",sum)
print("average",average)


#pro to take a tuple of numbers from keyboard and print Sum,average
x=tuple(map(float,input("enter a numbers").split()))
s =sum(x)
average=s/len(x)
print("sum:",s)
print("average",average)











