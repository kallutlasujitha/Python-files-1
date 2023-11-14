Biodata = {
    "name": "Krishna",
    "mother name": "devaki",
    "father name": "vasudeva",
    "designation": "king of dwaraka",
    "D.O.B": "acient years"
}
print(Biodata)


Biodata = {
    "name": "Krishna",
    "mother name": "devaki",
    "father name": "vasudeva",
    "designation": "king of dwaraka",
    "D.O.B": "acient years"
}
print(Biodata["name"])


Biodata = {
    "name": "Krishna",
    "mother name": "devaki",
    "father name": "vasudeva",
    "designation": "king of dwaraka",
    "D.O.B": "acient years"
}
Biodata["name"]="kannaya"
print(Biodata)


Biodata = {
    "name": "Krishna",
    "mother name": "devaki",
    "father name": "vasudeva",
    "designation": "king of dwaraka",
    "D.O.B": "acient years"
}
Biodata["name"]="kannaya"
Biodata["mother name"]="yashodha"
Biodata["father name"]="nandhudu"
print(Biodata)


#Biodata = {
    #"name": "Krishna",
    #"mother name": "devaki",
    #"father name": "vasudeva",
    #"designation": "king of dwaraka",
    #"D.O.B": "acient years"
#}
#Biodata["name","mother name","father name"]="kannaya","yashodha","nandhudu"
#print(Biodata)


Biodata = {
    "name": "Krishna",
    "mother name": "devaki",
    "father name": "vasudeva",
    "designation": "king of dwaraka",
    "D.O.B": "acient years"
}
del Biodata["father name"]
print(Biodata)

#IF YOU WANT TO DELETE ALL KEYS IN DICTIONARY YOU USE CLEAR() FUNCTION.
Biodata = {
    "name": "Krishna",
    "mother name": "devaki",
    "father name": "vasudeva",
    "designation": "king of dwaraka",
    "D.O.B": "acient years"
}
Biodata.clear()
print(Biodata)


#Biodata = {
    #"name": "Krishna",
    #"mother name": "devaki",
    #"father name": "vasudeva",
    #"designation": "king of dwaraka",
    #"D.O.B": "acient years"
#}
#del Biodata["name","mother name","father name","designation","D.O.B"]
#print(Biodata)




Biodata = {
    "name": "Krishna",
    "mother name": "devaki",
    "father name": "vasudeva",
    "designation": "king of dwaraka",
}
del Biodata["father name"]
print(Biodata)
if "father name" in Biodata:
    print("True")
else:
    print("false")