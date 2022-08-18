import sys

sys.stdin = open('input.txt')

for test_case in range(1, 11):
    N, num = map(str, input().split())

    stack = []

    for char in num:
        if not stack:
            stack.append(char)
        elif stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)

    print(f"#{test_case} {''.join(stack)}")