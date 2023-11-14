#{LIST}REMOVE[IN-BUILT]-1
s=[10,20,30,40,50,60,100,400,500]
s.remove(100)
print(s)

#{LIST}REMOVE[IN-BUILT]-2
s=[10,20,30,40,50,60,100,400,500,100]
s.remove(100)
print(s)

#{LIST}REMOVE[IN-BUILT]-3
s=['Lily','Rose','jas','marie','tulip']
s.remove('jas')
print(s)

#{LIST}REMOVE[IN-BUILT]-4
s=['Lily','Rose','jas','marie','tulip',"jas"]
s.remove('jas')
print(s)

#{LIST}REMOVE[IN-BUILT]-5
s=['Lily','Rose',['jas','marie'],'tulip',"jas"]
s.remove('jas')
print(s)