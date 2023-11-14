# Reverse a given integer number.
rev=0
a=int(input("enter a number"))#4321
while a>0:
    b=a%10  #4,3,2,1 #modular=it takes reminder.
    rev=rev*10+a%10  #0*10+4=4
    a//=10  #  floor=it takes quotient before point values.
print(rev)

# Reverse a given integer number.
a=int(input("enter a number"))
print(str(a)[::-1])