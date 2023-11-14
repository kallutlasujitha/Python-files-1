#LSPLIT(IN-BUILT)-1:
string = "   geeksforgeeks" #space removed
print(string.lstrip())

#LSPLIT(IN-BUILT)-2:
string = "++++x...y!!z*geeksforgeeks"
print(string.lstrip("+.!*xyz for"))

#LSPLIT(IN-BUILT)-3:
string = "++++x...y!!z* geeksforgeeks"
print(string.lstrip("+.!*xyz"))

#LSPLIT(IN-BUILT)-4:
string = "++++x...y!!z* geeks for geeks"
print(string.lstrip("+.!*xyz geeks for"))

#LSPLIT(IN-BUILT)-5:
string = "++++x...y!!z*geeksforgeeksgoogle"
print(string.lstrip("+.!*xyz geeks for"))

#LSPLIT(IN-BUILT)-6:
string = "++++x...y!!z*geeksforgeeksbanana"
print(string.lstrip("+.!*xyz geeks"))

#LSPLIT(IN-BUILT)-7:
string = "geeks for geeks"
print(string.lstrip('ge'))