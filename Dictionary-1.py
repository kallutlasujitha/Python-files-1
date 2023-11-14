
def returnSum (myDict):
    list = []
    for i in myDict:
        list.append(myDict[i])
    final = sum(list)
    return final
dict={'a':100, 'b':200, 's':300}
print("sum:", returnSum(dict))    




def returnSum (dict):
    sum = 0
    for i in dict.values():
        sum = sum+i
    return sum
dict={'a':100, 'b':200, 's':300}
print("sum:", returnSum(dict))




def returnSum (dict):
    return sum(dict.values())
dict={'a':100, 'b':200, 's':300}
print("sum:", returnSum(dict))



def returnSum(myDict):
    return sum(myDict[key]for key in myDict)
dict={'a':100, 'b':200, 's':300}
print("sum:", returnSum(dict))
