#{LIST}INSERT[IN-BUILT]-1
#insert=adding an element at the specified position.
#append=adding element at the end of the list.
s=[]
s.append(10)
s.append(20)
s.append(30)
s.append(40)
s.append(50)
s.append(60)
s.insert(3,800)     #list.insert(index,element)
print(s)

#{LIST}INSERT[IN-BUILT]-2
s=[10,20,30,40,50,60]
s.insert(3,800)
s[1]=15
print(s)

#{LIST}INSERT[IN-BUILT]-3
s=[10,20,30,40,50,60]
s.insert(3,800)
s[1]=15
s.append(900)
print(s)

#{LIST}INSERT[IN-BUILT]-4
s=[10,20,30,40,50,60]
s.append(700)
s.insert(10,800)
s[1]=15
print(s)

#{LIST}INSERT[IN-BUILT]-5
s=[10,20,30,40,50,60]
s.insert(10,800)
s[2]=15
s.append(700)
print(s)

#{LIST}INSERT[IN-BUILT]-6
s=[10,20,30,40,50,60]
s.insert(10,800)
s[1]=15
s.append(900)
print(s)

#{LIST}INSERT[IN-BUILT]-7
s=[10,20,30,40,50,60]
s.append(900)
s.insert(10,800)
s[4]=15
print(s)

#{LIST}INSERT[IN-BUILT]-8
s=[10,20,30,40,50,60]
s.insert(-10,800)
s[3]=15
s.append(900)
print(s)
