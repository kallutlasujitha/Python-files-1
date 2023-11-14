def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
x=int(input("enter a number"))
y=int(input("enter a number"))
print(add(x,y),sub(x,y),mul(x,y),div(x,y))




def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
print("please select operation -\n" \
      "1.add\n" \
      "1.sub\n" \
      "1.Mul\n" \
      "1.div\n")
select= int (input("select operation form 1,2,3,4"))
num_1=int(input("enter a number"))
num_2=int(input("enter a number"))
if select == 1:
    print(num_1, "+", num_2, "=", add(num_1,num_2))
if select == 2:
    print(num_1, "-", num_2, "=", sub(num_1,num_2))
if select == 3:
    print(num_1, "*", num_2, "=", mul(num_1,num_2))
if select == 4:
    print(num_1, "/", num_2, "=", div(num_1,num_2))   




