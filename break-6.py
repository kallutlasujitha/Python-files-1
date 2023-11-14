for i in range(2,500):
    out = 'prime'
    for j in range(2,i):
        if i%j == 0:
            out = 'not prime'
            break
    if out == 'prime':
        print(i)
