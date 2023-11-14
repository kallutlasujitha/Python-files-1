# class emp:
#     def __init__(self):
#         self.empno=222
#         self.ename='lilly'
# e=emp()
# print(e.__dict__)


# class emp:
#     def __init__(self):
#         self.a=222
#     def m1(self):
#         self.b=40
# e=emp()
# print(e.__dict__)
# e.m1()
# print(e.__dict__)
# e.c=90
# print(e.__dict__)



# class emp:
#     def __init__(self):
#         self.a=222
#     def m1(self):
#         self.b=40
# e=emp()
# e2=emp()
# e.m1()
# e2.r=200
# e.o=600
# print(e.__dict__)
# print(e2.__dict__)



class emp:
    x=20
    def __init__(self):
        self.a=30
        self.b=40
e=emp()
e.b=44
e.c=55
emp.a=999
t2=emp()
print(e.a,e.b,e.c)
print(t2.a,t2.b,t2.x)