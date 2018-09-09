import random
r = random.randint(1, 100)
while True:
    ques = input('guess number from 1~100: ')
    ques = int(ques)
    if ques == r:
        print('You are right!')
        break
    else:
        if ques > r:
            print('your number is bigger than it')
        elif ques < r:
            print('your number is smaller than it')