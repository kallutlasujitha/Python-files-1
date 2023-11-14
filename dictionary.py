d = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(d)


d={}
d[1]="ant"
d[2]="bat"
d["cat"]=10
print(d)


d=dict
a=(1,2,3)
b=("aman","boy","edge","king")
print(d.fromkeys(a,b))


# d=dict
# a=(1,2,3)
# b=("aman","boy","edge","king")
# c=(10,20,30)
# print(d.fromkeys(a,b,c))



d = dict(a= 10, b= 40, c= 70)
print(d)

#DEL(): it will be deleted particular key value 
#VAR[KEY]:it will be added particular key value
#CLEAR():it will be deleted all & gives output as "empty dict"{}
d={1:"apple",2:"ball",3:"cat"}
print(d)
del d[2]
print(d)
d[2]="bat"
print(d)
d.clear()
print(d)
print(d.clear())#if you give like this output as "NONE"


#single single will not be consider the set of tuples
# d=dict((1,"bat"),(2,"cat"),(3,"rat"),(4,"sat"))
# print(d)


#it takes list of tuple,so it will be consider
d=dict(((1,"bat"),(2,"cat"),(3,"rat"),(4,"sat")))
print(d)


#list of tuples will be consider
d=dict([(1,"bat"),(2,"cat"),(3,"rat"),(4,"sat")])
print(d)


d=dict({(1,"bat"),(2,"cat"),(3,"rat"),(4,"sat")})
print(d)


d=dict(((1,"bat"),(2,"cat"),(3,"rat"),(4,"sat")))
print(d.keys())
print(d.values())
print(d.items())
print(d.popitem())
print(d.popitem())
print(d.popitem())
print(d.popitem())
# print(d.popitem()): it will give output as "dictionary is empty"


#it will be give as output "Unhashable error".    
#REASON:you can't take the list of key & values
# d=dict({[1,"bat"],[2,"cat"],[3,"rat"],[4,"sat"]})
# print(d)


d=dict(a=[10,20,30],b=["ant","axe","ape"],c=[10,"ass",20])
print(d)
print(d.get('b'))


#doesn't perform any action, so it will give output as "NONE"
a={1:10,2:"bat",3:20}
b={1:30,2:"cat",3:40}
print(a.update(b))


#it will give output like this {1:30,2:"cat",3:40}
#REASON:we didn't change the keys, if keys will be same and if you give update function,
#then values will be changed to updated variable.
a={1:10,2:"bat",3:20}
b={1:30,2:"cat",3:40}
a.update(b)
print(a)


a={1:10,2:"bat",3:20}
b={4:30,5:"cat",6:40}
a.update(b)
print(a)


a={1:10,2:"bat",3:20}
b={4:30,5:"cat",6:40}
b.update(a)
print(b)


s={a:a*a for a in range(1,10)}
print(s)


n=int(input("enter a number"))
s={a:a*a for a in range(1,n+1)}
print(s)

