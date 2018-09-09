import random
r = random.randint(1, 100)
count = 0 # 計數
while True:
    count += 1 # 等於 count = count + 1
    ques = input('guess number from 1~100: ')
    ques = int(ques)
    if ques == r:
        print('You are right!')
        print('this is', count, 'times you guess')
        break
    else:
        if ques > r:
            print('your number is bigger than it')
        elif ques < r:
            print('your number is smaller than it')
    print('this is', count, 'times you guess')