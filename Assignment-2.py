a="abbbcccdddeeefffgghh"
count= {}
for i in a:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
for char,count in count.items():
    print(f"'{char}' occurs {count} times")