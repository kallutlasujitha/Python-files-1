#it gives output int object is not iterable
#s={10,20,30,40,50}
#s.update(60)
#print(s)

#{set} UPDATE [in-built]-1
s={"krishna","radha","rukmini","sathyabama"}
t=s.update()
print(t)

#{set} UPDATE [in-built]-2
l={60,70,80,80}
s={10,20,30,40,50}
s.update(l)
print(s)

#{set} UPDATE [in-built]-3
s={10,20,30,40,50}
s.update("aman")
print(s)

#{set} UPDATE [in-built]-4
l={"dharma","bheema","arjuna","nakula","sahadeva"}
s={10,20,30,40,50}
s.update(l)
print(s)

#{set} UPDATE [in-built]-5
l=["dharma","bheema","arjuna","nakula","sahadeva"]
t=(10,20,30,40,50)
s1={"panchali",10,"subadhra"}
s.update(l,t,s1)
print(s)


#{set} UPDATE [in-built]-6
l=["dharma","bheema","arjuna","nakula","sahadeva"]
t=(10,20,30,40,50)
s1={"panchali","subadhra"}
s={60,70,80,90}
s.update(l,t,s1,range(1,30))
print(s)