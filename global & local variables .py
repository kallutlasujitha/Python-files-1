#the variable which should declare outside the function
a=10
b=20
def f1():
    print("f1",a)
def f2():
    print("f2",b)
f1()
f2()

#the variable which should declare Inside the function
def f1():
    a=10
    print("f1",a)
def f2():
    b=20
    print("f2",b)
f1()
f2()


def f1():
    a=10
    b=20
    print("f1",a,b)
def f2():
    b=20
    print("f2",b)
f1()
f2()


#Here a is 10 but it changes to 20 because you write global of "a" inside
def f1():
    global a
    a=20
    print("f1",a)
def f2():
    print("f2",a)
f1()
f2()


#in this f1(10,20) and f1(20) will be printed because most preference taken local variable
a=10
b=10 
def f1():
    a=10
    b=20
    print("f1",a,b)
def f2():
    b=20
    print("f2",b)
f1()
f2()

#Here we write so many "a" values but it taken a is 60 for "f1"
#reason:it takes last preference
a=40
def f1():
    a=20
    a=40
    a=60
    print("f1",a)
def f2():
    print("f2",a)
f1()
f2()

