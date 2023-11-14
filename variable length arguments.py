# #if you write "star with any variable in the place of parameters" it will be taken as single tuple.

# def f1(*p):
#     print(p)
# f1(10,20,"roses")

# f1() takes 1 positional argument but 3 were given
def f1(p):
    print(p)
f1(10,20,"roses")


# def f1(*p):
#     print(sum(p))
# f1(10,20,30,40)


# def f1(*p):
#     count=0
#     for i in p:
#         count=count+i
#     print(count)
# f1(10,20,30,40)



# def f1(a="tuple",b="suji",*p):
#     count=0
#     for i in p:
#         count=count+i
#     print(a,b,"the sum of tuple values", count)
# f1(10,20,30,40)



# def f1(a,*p):
#     count=0
#     for i in p:
#         count=count+i
#     print(a,"the sum of tuple values",count)
# f1(10,20,30,40)



# def f1(a,*p):
#     count=0
#     for i in p:
#         count=count+i
#     print(a,"the sum of tuple values",count)
# f1(10,20,30,40,a="lilly")