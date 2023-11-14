a="abbbcccdddeeefffgghh"
vowels= {'a':0,'e':0,'i':0,'o':0,'u':0}
for i in a:
    j=i.lower()
    if j in vowels:
        vowels[j]+=1
for vowel, count in vowels.items():
    print(f"'{vowel}' occurs {count} times")