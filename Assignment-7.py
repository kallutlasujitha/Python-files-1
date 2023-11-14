
# def fact(n):
#     return 1 if (n==1 or n==0) else n*fact(n-1)
# n=5
# print(fact(n))


def fact(n):
    if (n==1 or n==0):
        return 1
    else: 
        a=n*fact(n-1)
    return a
n=5
print(fact(n))