#syntax= reduce(function,sequence)

#from functools import reduce
from functools import*
s=[1,2,3,4]
x=reduce(lambda a,b:a+b,s)
print(x)


s=[10,20,30,40,50]
y=reduce(lambda a,b:a+b,s)
print(y)


s=['s','u','j','i']
y=reduce(lambda a,b:a+b,s)
print(y)

