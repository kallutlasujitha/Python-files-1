s = input("enter a string:")
p = 0
for i in s:
    print("the char present at  the positive index is ",p,"is",i,"and at -ve index",p-len(s),"is",i)
    p+=1