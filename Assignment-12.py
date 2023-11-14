# Append new string in the middle of a given string.
a=input()
b=input()
mid=len(a)//2
x=a[:mid]+b+a[mid:]
print(x)

# Append new string in the middle of a given string.
l="suji kallutla"
middlestring="tha"
t=l.split()
middleposition=len(t)//1
s=t[:middleposition] +[middlestring]+t[middleposition:]
d=" ".join(s)
print(+str(d))
