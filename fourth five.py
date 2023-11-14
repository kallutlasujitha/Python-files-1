def f1(n):
    a=0
    b=1
    if n==1:
        print(a)
    else:
        print(a,end=',')
        print(b,end=',')
        for i in range(2,n):
            c=a+b
            a=b
            b=c
            print(c,end=',')
f1(10)


def assign(dict):
    sum = 0
    for i in dict:
        sum = sum+dict[i]
    return sum
dict={'a':100, 'b':200, 's':300}
print("sum:", assign(dict))



def fact(n):
    if (n==1 or n==0):
        return 1
    else: 
        a=n*fact(n-1)
    return a
n=5
print(fact(n))



def square(a):
    b=a**2
    return b
a=5
print("square",square(a))



students={'A':[10,20,30,40,50,60],'B':[20,30,40,50,60,70]}
a=input ("enter a student name")
if a in students.keys():
    print(students[a])
else:
    print("no student name in keys")