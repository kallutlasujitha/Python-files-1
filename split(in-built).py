#SPLIT[IN-BULIT]:1
x="strawberry"
y=x.split()
print(y)

#SPLIT[IN-BULIT]:2
p="split is a string in built function"
q=p.rsplit()
print(q)

#SPLIT[IN-BUILT]:3
p="split-is-a-string,in built function"
q=p.split("-")
print(q)

#SPLIT[IN-BUILT]:4
p="split-is-a-string,in,built,function"
q=p.split(",")
print(q)

#SPLIT[IN-BUILT]:5
p="split-is-a-string,in,built,function"
q=p.split(",")
for r in q: 
    print(r)

#SPLIT[IN-BUILT]:6
num="10 20 30 40 50 60 70"
p=num.split()
print(p)
