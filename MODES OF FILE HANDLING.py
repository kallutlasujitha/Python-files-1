

# try:
#     print(10/3)#statment-1
#     print(10/4)#statment-2
#     print(10/2)#statment-3
# except :
#     print("except block")#statment-4
# else:
#     print("else")#statment-5
# finally:
#     print("finally")#statment-6
# print("outside the block")#statment-7


# try:
#     print(10/0)#statment-1
#     print(10/3)#statment-2
#     print(10/2)#statment-3
# except ZeroDivisionError:
#     print("except block")#statment-4
# else:
#     print("else")#statment-5
# finally:
#     print("finally")#statment-6
# print("outside the block")#statment-7


# try:
#     print(10/0)#statment-1
#     print(10/3)#statment-2
#     print(10/2)#statment-3
# except ValueError:
#     print("except block")#statment-4
# else:
#     print("else")#statment-5
# finally:
#     print("finally")#statment-6
# print("outside the block")#statment-7


# try:
#     print(10/3)#statment-1
#     print(10/0)#statment-2
#     print(10/2)#statment-3
# except ZeroDivisionError:
#     print("except block")#statment-4
# else:
#     print("else")#statment-5
# finally:
#     print("finally")#statment-6
# print("outside the block")#statment-7 


# try:
#     print(10/3)#statment-1
#     print(10/0)#statment-2
#     print(10/2)#statment-3
# except ValueError:
#     print("except block")#statment-4
# else:
#     print("else")#statment-5
# finally:
#     print("finally")#statment-6
# print("outside the block")#statment-7


# try:
#     print(10/3)#statment-1
#     print(10/4)#statment-2
#     print(10/0)#statment-3
# except ZeroDivisionError:
#     print("except block")#statment-4
# else:
#     print("else")#statment-5
# finally:
#     print("finally")#statment-6
# print("outside the block")#statment-7 


# try:
#     print(10/3)#statment-1
#     print(10/4)#statment-2
#     print(10/0)#statment-3
# except ValueError:
#     print("except block")#statment-4
# else:
#     print("else")#statment-5
# finally:
#     print("finally")#statment-6
# print("outside the block")#statment-7

# try:
#     print(10/3)#statment-1
#     print(10/4)#statment-2
#     print(10/2)#statment-3
# except :
#     print(10/0)#statment-4
#     print("except block -2")#statment-5
# else:
#     print("else")#statment-6
# finally:
#     print("finally")#statment-7
# print("outside the block")#statment-8


# try:
#     print(10/3)#statment-1
#     print(10/4)#statment-2
#     print(10/2)#statment-3
# except ZeroDivisionError:
#     print("except block")#statment-4
#     print(10/0)#statment-5
# else :
#     print("else")#statment-6
# finally:
#     print("finally")#statment-7
# print("outside the block")#statment-8


# try:
#     print(10/3)#statment-1
#     print(10/4)#statment-2
#     print(10/2)#statment-3
# except ZeroDivisionError:
#     print("except block")#statment-4
#     print("except block-2")#statment-5
# else :
#     print(10/0)#statment-6
# finally:
#     print("finally")#statment-7
# print("outside the block")#statment-8


f=open("suji.txt","r")
print(f.read())

# f=open("doc.txt","r")
# print(f.read())


# f=open("suji.txt","w")
# print(f.write("suji"))


# f=open("sujitha.txt","w")
# print(f.write("sujitha"))


# f=open("suji.txt","w")
# print(f.read())


# f=open("suji.txt","a")
# print(f.append())

# f=open("suji.txt","a")
# print(f.append("rose"))


# f=open("suji.txt","x")
# print(f.exclusive())


# f=open("suji.txt","w")
# print(f.name)
# print(f.mode)
# print(f.closed)
# print(f.readable())
# print(f.writable())




#f.write(str)
#f.writelines(list line by lines)

# f=open("suji.txt","w")
# f.write("All roses are")
# f.write(" not in same colour")
# f.write(" but roses are beautiful")


# f=open("suji.txt","w")
# l=["All is well"]
# f.writelines(l)


# f=open("suji.txt","w")
# l=["All\n", "is\n", "well\n"]
# print(len(l))
# f.writelines(l)


# f=open("suji.txt","w")
# l=("All\n", "is\n", "well\n")
# print(len(l))
# f.writelines(l)
# f.close()



#HOW TO READ CHAR FROM THE FILE
#READ()=to read total data from the file
#READ(n)=to read n char from the file
#READLINE()=if i want to read line
#READLINES()=to read all lines in the list

#READ():
# f=open("sujitha.txt","r")
# print(f.read())


#READ(n):

# f=open("sujitha.txt","r")
# print(f.read(50))

# f=open("sujitha.txt","r")
# print(f.read(10))

# f=open("sujitha.txt","r")
# print(f.read(100))

#READLNE():
# f=open("sujitha.txt","r")
# print(f.readline(10))

# f=open("sujitha.txt","r")
# print(f.readline(20))

# f=open("sujitha.txt","r")
# print(f.readline(35))

# f=open("sujitha.txt","r")
# print(f.readline())
# print(f.readline())
# print(f.readline())


#READLINES():

# f=open("sujitha.txt","r")
# print(f.readlines())

# f=open("sujitha.txt","r")
# print(f.readlines(10))



#TELL():IT RETURNS THE POSITION WHERE THE CURSOR IS SET TO BEGIN READING
# it returns the current file position in a file stream
# SYNTAX: FILE.TELL()

# f=open("suji.txt","r")
# print(f.readlines())
# print(f.tell())


#SEEK(): IT IS USED TO SET THE POSITION OF THE FILE CURSOR
#  it change the current file position in a file stream
# SYNTAX:FILE.SEEK(OFFSET)

# f=open("suji.txt","r")
# f.seek(4)
# print(f.readlines())


# f=open("suji.txt","r")
# f.seek(4)
# print(f.readlines())
# print(f.tell())


# f=open("suji.txt","r")
# print(f.seek(4))

# mode="r"
# if mode=="r"
# print(f"name:{student_name}")



# # Define student details
# student_name="suji"
# roll_number="12345"
# age="22"
# marks=90
# grade="a+"
# # Define the mode
# mode = "basic"
# # Define the filename
# filename = "student_details.txt"
# # Open the file for writing
# with open(filename, "w") as f:
#     if mode == "basic":
#         f.write(f"Name: {student_name}\n")
#         f.write(f"Roll Number: {roll_number}\n")
#     elif mode == "full":
#         f.write(f"Name: {student_name}\n")
#         f.write(f"Roll Number: {roll_number}\n")
#         f.write(f"Age: {age}\n")
#         f.write(f"marks:{marks}\n")
#         f.write(f"Grade: {grade}\n")
#     else:
#         print("Invalid mode. Please use 'basic' or 'full'.")
# # Open the file for reading and print its content
# with open(filename, "r") as f:
#     print(f.read())
#     print(f.read(5))
#     print(f.readline())
#     print(f.readline(50))
#     print(f.readlines())
#     print(f.readlines(10))
#     print(f.readlines(11))
#     print(f.mode)
#     print(f.closed)
#     print(f.readable())
#     print(f.writable())
#     f.close()
# with open(filename, "w") as f:
#     print(f.write("something"))
#     print(f.writelines("basic"))
#     print(f.name)
#     print(f.mode)
#     print(f.closed)
#     print(f.readable())
#     print(f.writable())



# student_name="suji"
# roll_number="12345"
# age="22"
# marks=90
# grade="a+"

# student_name="nani"
# roll_number="54321"
# age="25"
# marks=90
# grade="a+"




# a=[a=input("name")
# b=input("roll_number")
# c=input("age")
# d=input("grade")
# e=input("marks")]
# filename="student_details.txt"
# with open(filename,"w") as file:
#     student_data= file.write(a)#here wrong
# student_records= student_data.split("\n\n")
# for i in student_records:
#     print(i)
#     print("\n")





    