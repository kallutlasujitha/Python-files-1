#LIST COMPREHENSION-1
a=[10,20,10,40,10,]
l=[x for x in a]
print(l)

#LIST COMPREHENSION-2
a=["grapes",20,"mango",40,"apple",]
l=[x for x in a if "a" if x]
print(l)

#LIST COMPREHENSION-3
a=[10,20,10,40,10,]
l=[x for x in a if x!=10]
print(l)

#LIST COMPREHENSION-4
a=["go","went","gone"]
l=[x.upper() for x in a]
print(l)

#LIST COMPREHENSION-5
l=[i for i in range(1,30)]
print(l)

#LIST COMPREHENSION-6
l=[i for i in range(1,30) if i<5]
print(l)

#LIST COMPREHENSION-7
l=[i**3 for i in range(1,30)]
print(l)

#LIST COMPREHENSION-8
l= [i%2==0 for i in range(1,30) ]
print(l)







