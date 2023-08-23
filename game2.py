
import random

pick = ['가위', '바위', '보']
computer = {0: '이겼다!', 1: '졌다..', 2: '비겼다.'}


def check(user, com):

    if not user in pick:
        print('잘못입력했습니다. 다시 입력 해주세요')
        return False

    print(f'사용자 ( {user} vs {com} ) 컴퓨터')
    if user == com:  # 0 1 2 > result
        state = 2
    elif user == '가위' and com == '바위':
        state = 1
    elif user == '바위' and com == '보':
        state = 1
    elif user == '보' and com == '가위':
        state = 1
    else:
        state = 0
    print(computer[state])
    return True


def regame():
    while True:
        user = input("다시하시겠습까? : O , X ")
        if user == 'O':
            return True
        elif user == 'X':
            return False
        else:
            print("O 또는 X를 입력하세요.")


print('\n-------------------------------------------')
while True:
    user = input("가위, 바위, 보 : ")
    com = pick[random.randint(0, 2)]
    if check(user, com):
        if regame():
            continue
        else:
            break
print('-------------------------------------------\n')
