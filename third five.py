# def f1(a):
#     b=a.split()
#     out={}
#     for i in range(1,len(b)+1):
#         out[i]=b[i-1]
#     print(out)
# f1(['Roses are red'])



# a='Roses are red'
# b=a.split()
# out={}
# for i in range(1,len(b)+1):
#     out[i]=b[i-1]
# print(out)


def f1(a):
    print(a.split())
f1('i am a genius')


def f1(a):
    out=''
    i=2
    for i in range(len(a)):
        if i%2==0:
            out+=a[i]
    print(out)
f1('roses are red')



for i in range(0,51):
    if i %2==0:
        print(i,end=",")


def f1():
    for i in range (0,51):
        if i%2==0:
            print(i,end=',')
f1()


def f1(a):
    for i in range (0,a+1):
        if i%2==1:
            print(i,end=',')
num=int(input('enter a number'))
f1(num)



