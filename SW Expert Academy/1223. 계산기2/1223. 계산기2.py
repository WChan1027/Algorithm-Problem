import sys

sys.stdin = open('input.txt')

for test_case in range(1, 11):
    N = int(input())
    string = input()
    operator = ['+', '-', '*', '/']
    stack = []
    result = ''

    for i in string:
        if i in '+-':
            if stack and stack[-1] in '+-':
                result += stack.pop()
                stack.append(i)
            elif stack and stack[-1] in '*/':
                result += stack.pop()
                if stack:
                    result += stack.pop()
                stack.append(i)
            else:
                stack.append(i)
        elif i in '*/':
            if stack and stack[-1] in '+-':
                stack.append(i)
            elif stack and stack[-1] in '*/':
                result += stack.pop()
                stack.append(i)
            else:
                stack.append(i)
        else:
            result += i
    while stack:
        result += stack.pop()

    stack = []

    for i in result:
        if i not in operator:
            stack.append(i)
        else:
            if i == '+':
                a = int(stack.pop()) + int(stack.pop())
                stack.append(a)
            elif i == '-':
                a = int(stack.pop()) - int(stack.pop())
                stack.append(a)
            elif i == '*':
                a = int(stack.pop()) * int(stack.pop())
                stack.append(a)
            elif i == '/':
                a = int(stack.pop()) / int(stack.pop())
                stack.append(a)

    answer = stack.pop()

    print(f'#{test_case} {answer}')