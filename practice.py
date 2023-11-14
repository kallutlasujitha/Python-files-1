#rows=[i for i in (6) for j in (i+1)]
#print("*",end=" ")

x="abbccdefag"
l=[]
for i in x:
    if i not in l:
        l.append(i)
x="".join(l)
print(x)


