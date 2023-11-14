
#PATTERN=6.1
rows = 6
ascii_value = 65
for i in range(rows):
    for j in range(i+1):
        alphabet = chr(ascii_value)
        print(alphabet, end=" ")
    ascii_value += 1
    print("")


#PATTERN=6.2
rows = 7
ascii_value = 71
for i in range(rows,0,-1):
    for j in range(1,i+1):
        alphabet = chr(ascii_value)
        print(alphabet, end=" ")
    ascii_value -= 1
    print("")