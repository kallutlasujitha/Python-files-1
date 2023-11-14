# import time
# from imp import reload 
# import module
# import module
# import module
# import module
# import module  #if you write multiple times it will give output as single time
# print("hey,what r u doing")
# time.sleep(20)
# reload(module)
# import module
# print("i'm learning python") #if i'm write time before print it will give take time to print 

#if you change module data and then excuted it will give output as before 
#data only, because of that data came on pycache that's why it will give 
# before output.
#if you use reload, it will give output what u changed data.

#RANDOM():
#going to print between 0 and 1 (not inclusive)
from random import*
for i in range(10):
    print(random())

# for i in range(10):
#     print(random(4,9)) #IT'S NOT TAKEN ARGUMENTS,IF YOU GIVE OUTPUT AS ERROR


#RANDINT():(inclusive)
for i in range(10):
    print(randint(1,15))

for i in range(4):
    print(randint(1,15))

for i in range(10):
    print(randint(15,30))

for i in range(14):
    print(randint(1,15))


#UNIFORM():
#it returns random float values 1 to 0 and it is not inclusive
for i in range(10):
    print(uniform(1,20))


#RANDRANGE():
#randrange(start,stop,step)
#start value is optional default value is 0
#step value is optional default value is 0
#start value is inclusive and stop value is not inclusive
for i in range(10):
    print(randrange(1000,9999))

for i in range(4):
    print(randrange(1000,9999))

for i in range(10):
    print(randrange(10000,99999))

for i in range(4):
    print(randrange(100000,999999))