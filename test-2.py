import suji

print(suji.x)
print(suji.y)


from package1 import module1
print(module1.x)
print(module1.add)
print(module1.add(10,20))
print(module1.div(10,20))
module1.add(10,20)
module1.div(10,20)

# from package1 import x


from suji import x,y
print(x)
print(y)


import suji as rose
print(rose.x)

from package1 import module1 as rose
print(rose.x)

from package1 import module1 as rose
print(rose.add)


from suji import *

add(3,4)
print(x)
sub(4,3)

from suji import x,y,add,sub
add(11,22)
sub(44,4)
print(x)
print(y)


from suji import add as seed,sub as tree,mul as flower,div as fruit
seed(99,1)
tree(200,100)
flower(10,10)
fruit(200,2)


from suji import add as berry
berry(30,40)


from suji import x,y,add,sub
print(add(10,20))
print(sub(10,20))


from suji import div as lilly
lilly(10,20)


import suji


from package1 import module1
# from package1 import module2
# from package1 import module3

# from package1 import module1,module2,module3


#POSSIBILITIES:
#1. import module name
#2. import module1,module2,module3(at a time we import 3modules)
#3. import module1 as mad(instead of module name you can write alias name)
#4. import module1 as mad,module2 as bad,module3 as sad....(instead of module names you can write alias names at a time)
#5. from module import member
#6. from module import member1,member2,member3,.....
#7. from module import member1 as mad,member2 as bad,member3as sad,.....
#8. from module import *

