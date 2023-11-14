#PATTERN-5.1
rows = 6
for i in range(rows,0,-1):
    for j in range(0,i):
        print(j, end=' ')
    print("")

#PATTERN-5.2
rows = 5
for i in range(rows,0,-1):
    for j in range(i+1):
        print(i, end=' ')
    print("")