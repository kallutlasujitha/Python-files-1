# Calculate the cube of all numbers from 1 to a given number.
for i in range(1,20):
   j=i**3
   print(j,end=",")

# Calculate the cube of all numbers from 1 to a given number.
l=[pow(i,3) for i in range(1,20)]
print("enter a cube of numbers",l)

# Calculate the cube of all numbers from 1 to a given number.
l=int(input("enter a number"))
m=int(input("enter a number"))
#sum=0
for i in range(l,m+1):
   j=(i**3)
   #sum+=j
   #sum=sum(j)
   print(j,end=",") 


