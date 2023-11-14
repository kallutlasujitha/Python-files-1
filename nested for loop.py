for n in range (1,100):
    out = 0
    for i in range(1,n):
        if n%i == 0:
            out+=i
    if out == n:
        print(n)