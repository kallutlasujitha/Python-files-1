#{LIST}INDEX[IN-BUILT]-1
s=[20,30,40.5,50,60,100,101.20,60,50]
print(s.index(60))

#{LIST}INDEX[IN-BUILT]-2
s=[20,30,40.5,[50,60],100,101.20,60,50]
print(s.index(60))

#{LIST}INDEX[IN-BUILT]-3
s=[20,30,40.5,[50,60],100,101.20,[60,50],60]
print(s.index(60))

#{LIST}INDEX[IN-BUILT]-4
s=['Lily','Rose','jas','marie','tulip']
print(s.index('jas'))

#{LIST}INDEX[IN-BUILT]-5
s=['Lily',['Rose','jas'],'marie','tulip']
print(s.index('tulip'))

#{LIST}INDEX[IN-BUILT]-6
s=['Lily',['Rose','jas'],'marie','tulip']
print(s[1])

#{LIST}INDEX[IN-BUILT]-7
s=['Lily',['Rose','jas'],'marie','tulip']
print(s[1][1])