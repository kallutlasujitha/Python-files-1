# class Qualification:
#     def __init__(self,age,height,college,branch,marks,passedout,phoneno):
#         self.age = age
#         self.height = height
#         self.college = college
#         self.branch = branch
#         self.marks = marks
#         self.passedout = passedout
#         self.phoneno = phoneno
# sujitha = Qualification("22",5.0,"GIST","CE",8.0,2022,123456)
# supriya = Qualification("24",5.1,"SEC","ECE",8.0,2020,654321)
# print(supriya.branch)
# print(sujitha.branch)


# class Employee:
#     '''ths class is developed by rose'''
#     def __init__(self):
#        pass
# print(Employee.__doc__) 



# class Employee:
#     def __init__(self):
#         self.name="lilly"
#         self.id=9999
#         self.phno=54205
#         self.domain="python"
#         print("hai",self.name)
#         print("your Id",self.id)
#         print("and your number",self.phno)
#         print("this is your domain",self.domain)
# a=Employee()
# a.__init__



# class Employee:
#     def __init__(self):
#         self.name="lilly"
#         self.id=9999
#         self.phno=54205
#         self.domain="python"
#         print("hai",self.name)
#         print("your Id",self.id)
#         print("and your number",self.phno)
#         print("this is your domain",self.domain)
# a=Employee()
# print(a.id,a.name,a.phno,a.domain)
# a.__init__



# class Employee:
#     def __init__(self):
#         self.name="lilly"
#         self.id=9999
#         self.phno=54205
#         self.domain="python"
#     def say(self):
#         print("hai",self.name)
#         print("your Id",self.id)
#         print("and your number",self.phno)
#         print("this is your domain",self.domain)
# a=Employee()
# print(a)#it gives generator
# print(a.id)
# print(a.id,a.name,a.phno,a.domain)
# # Print(a.say)#gives name error
# a.say()


# class Employee:
#     def __init__(self,name,id,phno,domain):
#         self.name=name
#         self.id=id
#         self.phno=phno
#         self.domain=domain
#     def say(self):
#         print("hai",self.name)
#         print("your Id",self.id)
#         print("and your number",self.phno)
#         print("this is your domain",self.domain)
# a=Employee("lilly",9999,54205,"python")
# print(a)#it gives generator
# print(a.id)
# print(a.id,a.name,a.phno,a.domain)
# a.say()



#gives output second constructor,because it a updated one.
# class Test:
#     def __init__(self):
#         print("first constructor")
#     def __init__(self):
#         print("second constructor")
# a=Test()


class Test:
    def __init__(self):
        print("first constructor")
a=Test()
t1=Test()
t2=Test()

# def f1():
#     print("hello")


# class Don:
#     def Room(self):
#         print()