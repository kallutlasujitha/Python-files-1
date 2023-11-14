def assign(dict):
    sum = 0
    for i in dict:
        sum = sum+dict[i]
    return sum
dict={'a':100, 'b':200, 's':300}
print("sum:", assign(dict))