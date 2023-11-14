#HOW TO CHECK WHEATHER THE FILE IS AVAILABLE OR NOT


#wheather file is there it gives TRUE ,is not there it will give FALSE
# import os
# f=os.path.isfile("suji.txt")
# print(f)

# import os
# f=os.path.isfile("ammu.txt")
# print(f)

# f=open("filename","r")
# a=(f.read())
# print(a)

#WRITE A PROVTO SHOE THE CONTENT OF A FILE AND IF FILE NOT EXIST THEN TELL
#THE FILE IS NOT AVAILABLE.

# file_name=input("enter a file name")
# if file_name :
#     file=open(file_name,"r")
#     a=(file.read())
#     print(a)
# else:
#     print("file is not available")
# file.close()



# file_name=input("enter a file name")
# file=open(file_name,"r")
# if file:
#     a=(file.read())
#     print(a)
#     file.close()
# else:
#     print("file is not available")


#WRITE A PROVTO SHOE THE CONTENT OF A FILE AND IF FILE NOT EXIST THEN TELL
#THE FILE IS NOT AVAILABLE.

# file_name=input("enter a file name")
# try:
#     f=open(file_name,'r')
#     a=f.read()
#     print(a)
# except FileNotFoundError:
#     print("file not found")



#WRITE A PROGRAM TO PRINT A NUMBER OF LINES,WORDS AND CHARACTER PRESENT IN
#THE GIVEN FILE?

# file_name=input("enter a file name")
# lines=0
# words=0
# characters=0
# f=open(file_name,'r')
# for i in f:
#     lines +=1
#     words +=len(i.split())
#     characters =len(i)
# print("no of lines:",lines)
# print("no of words:",words)
# print("no of characters:",characters)

#HANDLING BINARY DATA

# a1=open("tree.jpg",'rb')
# a2=open("violettree.jpg",'wb')
# b=a1.read()
# a2.write(b)


# a1=open("th.jpg",'rb')
# a2=open("tree.jpg",'wb')
# b=a1.read()
# a2.write(b)


#WRITE A PROGRAM FOR HANDLING BINARY DATA FOR VIDEO FILE
# a1=open("video.mp4",'rb')
# a2=open("sample video.mp4",'wb')
# b=a1.read()
# a2.write(b)


















