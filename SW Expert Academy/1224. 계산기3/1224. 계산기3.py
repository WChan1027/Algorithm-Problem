import sys

sys.stdin = open('input.txt')

for test_case in range(1, 11):
    N = int(input())        # 테스트 케이스의 길이
    char = input()      # 테스트 케이스
    stack = []
    result = ''     # 후위 표기식

    # 후위 표기식으로 변환
    for i in char:
        if i in '+-*/()':       # 연산자일 때
            if not stack:       # stack이 비어있을 때
                stack.append(i)
            elif i in '*/':     # 곱셈/나눗셈일 때
                if stack[-1] in '*/':       # 이전 연산자가 곱셈/나눗셈이었을 때 (동일한 우선순위)
                    result += stack.pop()       # 이전 연산자를 처리
                stack.append(i)     # stack에 저장
            elif i in '+-':     # 덧셈/뺄셈일 때
                if stack[-1] != '(':        # 이전 stack이 괄호가 아닌 연산자일 때, 덧셈/뺄셈은 우선순위가 최하위이므로 이전 연산자를 처리
                    result += stack.pop()
                stack.append(i)     # stack에 저장
            elif i == '(':      # 괄호의 시작
                stack.append(i)
            elif i == ')':      # 괄호의 끝
                while stack and stack[-1] != '(':       # 괄호 안에 남은 연산을 처리
                    result += stack.pop()
                stack.pop()     # ( 제거
        else:       # 숫자일 때
            result += i

    # 후위 표기식을 이용해 연산
    for i in result:
        if i in '+-*/':     # 연산자일 때 stack의 위에 두 수를 연산
            a = int(stack.pop())
            b = int(stack.pop())
            if i == '+':
                stack.append(b + a)
            elif i == '-':
                stack.append(b - a)
            elif i == '*':
                stack.append(b * a)
            elif i == '/':
                stack.append(b // a)
        else:       # 숫자일 때 stack에 저장
            stack.append(i)

    answer = stack.pop()

    print(f'#{test_case} {answer}')