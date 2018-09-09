# 讓使用者決定隨機數範圍(起值與終值)

import random
start = input('decide random digit\'s start plz: ')
end = input('decide random digit\'s end plz: ')
start = int(start)
end = int(end)
r = random.randint(start, end)
count = 0 # 計數
while True:
    count += 1 # 等於 count = count + 1
    ques = input('guess numbers: ')
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