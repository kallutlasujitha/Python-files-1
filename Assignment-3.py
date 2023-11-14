#assignment-3.1{using loop} OUTPUT: VOWEL
a= input("enter a string")
vowels="AEIOUaeiou"
for i in a:
    if i in vowels:
        print("vowels present in the input :",",".join(i))

#assignment-3.2{using list comprehension}
a= input("enter a string")
vowels=[i for i in a if i in "AEIOUaeiou"]
#print(vowels)
print("vowels present in the input :",",".join(vowels))

#assignment-3.3(using list comprehension)
W=["AMAN","toNny","AMAN","tonny"]
b=[i[0].upper() for i in W]
print(b)

#assignment-3.4{using list comprehension}
W=["AMAN","toNny","AMAN","tonny"]
b=[j for i in W  for j in i if j.isupper()]
print(b)

#assignment-3.5{using loop}
W=["AMAN","toNny","AMAN","tonny"]
b=[]
for i in W:
    for j in i:
        #if j not in b:
        if j.isupper():
            b.append(j)
print(b)


