# Display Fibonacci series up to 10 terms.
n= int(input("enter range"))
a,b=0,1
i=0
while i<n:
    print(a,end=",")
    j=a+b
    a=b
    b=j
    i+=1
  

# Display Fibonacci series up to 10 terms
K= int(input("enter range"))
i,j=0,1
print(i,j,end=",")
for _ in range(K-2):
    x=i+j
    i=j
    j=x
    print(x,end=",")
