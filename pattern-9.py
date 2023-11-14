
#PATTERN=9.1
size = 6
for i in range(size):
    for j in range(size - i):
        print(" ", end="")
    for k in range(i+1):
        print("*", end="")
    print()

#PATTERN=9.2
size = 6
for i in range(size):
    for j in range(size - i):
        print(" ", end="")
    for k in range(i+1):
        print(i, end="")
    print()

#PATTERN=9.3
size = 6
for i in range(1,size):
    for j in range(size - i):
        print(" ", end="")
    for k in range(i):
        print(i, end="")
    print()   