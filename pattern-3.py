#PATTERN=3.1
rows = 6
for i in range(rows):
    for k in range(rows-i-1):
        print(end=' ')
    for j in range(i):
        print(i,end=' ')
    print('')

#PATTERN=3.2
rows = 6
for i in range(rows):
    for k in range(rows-i-1):
        print(end=' ')
    for j in range(i):
        print('*',end=' ')
    print('')