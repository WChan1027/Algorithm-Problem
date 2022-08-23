import sys

sys.stdin = open('sample_input.txt')

T = int(input())

for test_case in range(1, T+1):
    char = input().split()
    stack = []

    for i in char:
        if i.isdecimal():       # 숫자일 때
            stack.append(i)
        elif i in '+-*/':       # 연산자일 때
            if len(stack) > 1:
                if i == '+':
                    a = int(stack.pop())
                    b = int(stack.pop())
                    stack.append(a + b)
                elif i == '-':
                    a = int(stack.pop())
                    b = int(stack.pop())
                    stack.append(b - a)
                elif i == '*':
                    a = int(stack.pop())
                    b = int(stack.pop())
                    stack.append(a * b)
                else:
                    a = int(stack.pop())
                    b = int(stack.pop())
                    stack.append(b // a)
            else:       # 오류 / 연산자로 계산할 숫자가 없을 때
                answer = 'error'
                break
        elif i == '.':      # 연산 종료
            if len(stack) == 1:
                answer = stack.pop()
            else:       # 오류 / 처리되지 않은 숫자 or 연산자가 남았을 때
                answer = 'error'

    print(f'#{test_case} {answer}')