rows = 6
for i in range(rows):
    for k in range(rows-i-1):
        print(end=' ')
    for j in range(i):
        print('*',end=' ')
    print('')