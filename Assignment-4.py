students={'A':[10,20,30,40,50,60],'B':[20,30,40,50,60,70]}
a=input ("enter a student name")
if a in students.keys():
    print(students[a])
else:
    print("no student name in keys")



a= dict()
n=int(input("enter a number of students"))
for i in range (n):
    sname=input("enter a student name")
    marks=[]
    for j in range (5):
        mark=float(input("enter a student marks:"))
        marks.append(mark)
    a[sname]=marks
print("list of student marks=",a)