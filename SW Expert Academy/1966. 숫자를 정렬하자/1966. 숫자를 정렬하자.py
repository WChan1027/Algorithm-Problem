import sys

sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    num = list(map(int, input().split()))

    for j in range(N):
        for i in range(N-1):
            if num[i] > num[i+1]:
                num[i], num[i+1] = num[i+1], num[i]

    result = ''
    for i in range(len(num)):
        result += f'{num[i]} '
    print(f"#{test_case} {result}")