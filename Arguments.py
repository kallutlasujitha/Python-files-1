#positional arguments follows keyword arguments follows default arguments
def f1(a,b,c):
    print(a*b*c)
f1(10,20,30) #these 10,20,30 are the positional arguments

# #KEYWORD ARDUMENTS:
def f1(a,b,c):
    print("hai", a,"how are",b,c)
f1(a="lilly",b="you",c="girl")#if you write a="any thing " like this these are the keyword arguments


def f1(a,b,c):     
    print("hai", a,"how are",b,c)
f1(b="you",a="lilly",c="girl")#if you write keyword arguments as unorder it will take 



def f1(a,b,c):
    print("hai", a,"how are",b,c)
f1(a="lilly","you",c="girl")#why it gives error means always positional argument follows keyword argument



def f1(a,b,c):
    print("hai", a,"how are",b,c)
f1("lilly",b="you",c="girl")#here positional argument follows keyword argument,so it not shows error


#DEFAULT ARGUMENTS:
def f1(a="good day"):#a="good day" is a default argument
    print("hai do you want",a)
f1(a="biscuit")


def f1(a="good day"):#a="good day" is a default argument
    print("hai do you want",a)
f1()


def f1(a,b,c="lady"):
    print("hai", a,"how are",b,c)
f1(a="lilly",b="you")

#here keyword arguments doedn't follows default arguments
def f1(a,b,c="lady",d):
    print("hai", a,"how are",b,c,d)
f1("lilly",b="you",d="girl")


#here follows,positional arguments follows keyword arguments follows default arguments
def f1(a,b,c,d="girl"):
    print("hai", a,"how are",b,c,d)
f1("lilly",b="you",c="lady")

