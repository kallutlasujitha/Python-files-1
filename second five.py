def f1(a):
    if 0<=a<=9:
        print('given number is a single digit')
    elif 10<=a<=99 or -99<=a<=-10:
        print('given number is a double digit')
    elif 100<=a<=999 or -999<=a<=-100:
        print('given number is a triple digit')
    else:
        print('more than 3digit')
f1(-100)



def f1(a):
    if a%3==0:
        if a%5==0:
            print("sweet& hot")
        else:
            print("hot")
    elif a%5==0:
        print("sweet")
    else:
        print('number is not divisible by 3 & 5')
f1(int(input('enter a number')))



# def f1(*a):
#     if len(a)%2==1:
#         b=len(a)//2
#         print(b)
#         if a[b] in 'AEIOU':
#             print(a[b])
# f1(1,2,3,4,5)
       

def f1(*a):
    if type(*a)==list:
        if len(*a)%2==0:
            print("given collection is list & has even length")
        else:
            print("given collection is list but not even")
    else:
        print("collection is not a list")
f1([10,20,True,'hello','hai'])
