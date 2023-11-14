# downward triangle star pattern
#PATTERN=10.1
size = 5
for i in range(size):
    for j in range(i):
        print(" ", end="")
    for k in range(size, i, -1):
        print("*", end="")
    print()

#PATTERN=10.2
size = 5
for i in range(size):
    for j in range(i):
        print(" ", end="")
    for k in range(size, i, -1):
        print(i, end="")
    print()