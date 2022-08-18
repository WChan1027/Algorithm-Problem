import sys

sys.stdin = open('sample_input.txt')

T = int(input())

for test_case in range(1, T+1):
    code = input()
    bracket = ['{', '}', '(', ')']
    check = []
    # 주어진 코드에서 괄호를 리스트에 추가하고 정상적인 짝을 이루면 제거
    for i in code:
        if i in bracket:
            check += [i]
            if len(check) > 1 and check[-1] == bracket[1] and check[-2] == bracket[0]:
                check.pop()
                check.pop()
            elif len(check) > 1 and check[-1] == bracket[3] and check[-2] == bracket[2]:
                check.pop()
                check.pop()
    # 모든 괄호가 정상적인 짝을 이루고 제거되면 1, 그렇지 않으면 0 반환
    if len(check) == 0:
        answer = 1
    else:
        answer = 0

    print(f'#{test_case} {answer}')