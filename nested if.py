a = int(input('enter a number'))
if a%3 == 0:
    if a%5 == 0:
        print('hot & sweet')
    else:
        print('hot')
elif a%5 == 0:
    print('sweet')
else:
    print('not divisible by 5 or 3')