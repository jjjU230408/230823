import random

print('업다운게임시작')


random_number = random.randint(1, 100)
count = 1

while True:
    user = int(input('숫자 입력 : '))
    if user > random_number:
        print('DOWN')
        count += 1
    elif user < random_number:
        print('UP')
        count += 1
    elif user == random_number:
        break
print('정답! ' + str(count) + '회 만에 정답')
