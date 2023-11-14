#COUNT[IN-BUILT]:1
a="python is high level language and also interpreted language"
print(a.count("language"))

#COUNT[IN-BUILT]:2
a="python is high level language and also interpreted language"
print(a.count("language",0,59))

#COUNT[IN-BUILT]:3
a="python is high level language and also interpreted language"
print(a.count("language",0,40))

#COUNT[IN-BUILT]:4
a="python is high level language and also interpreted language"
print(a.count("language",21,40))

#COUNT[IN-BUILT]:5
a="python is high level language and also interpreted language"
print(a.count("language",21,59))

#COUNT[IN-BUILT]:6
a="python is high level language and also interpreted language"
print(a.count("language",0,len(a)))

#COUNT[IN-BUILT]:7
a="python is high level language and also interpreted language"
print(a.count("language",21,len(a)))