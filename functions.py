#FUNCTION SYNTAX:
#def fname(args):
    #statment block
    #return val1,...valn
#fname(args) or var=fname(args)
#print(fname(args)) or print(var)


#def converttoCapitals(name):
    #nameCaps=name.upper()
    #return(nameCaps)
#name = input("enter your name")
#callingtheFunction=converttoCapitals(name)
#print(callingtheFunction)


def bio():
    name="sujitha"
    rollno = "182U1A0130"
    qualification ="BTech"
    Branch="civil"
    print(name,rollno,qualification,Branch)
a=bio()
print(a)



def name(fname):
    print("sujitha " + fname)
name("email")
name("phone no")
name("employee id")



def name(*kids):
    print("the youngest child is " +kids[1])
name("supriya","sujitha")



def add(num1: int, num2: int):
    num3=num1+num2
    return num3
num1,num2=2,3
ans=add(num1,num2)
print(f"the addition of {num1} and {num2} is {ans}")


# def program(n,a):
# #print(a,end=" ")
#     for n in a :
#         if n == 0:
#             break
#         if 1<=n<=50:
#             if n in a:
#                 a.remove(n)
#                 print('deleted')
#             else:
#                 print('out of range')
#     return(a)
# a=list(range(1,51))
# n = int(input('enter a number'))
# result=program(n,a)
# print(result)