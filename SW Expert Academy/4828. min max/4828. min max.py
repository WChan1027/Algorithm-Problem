import sys

sys.stdin = open('input.txt')

T = int(sys.stdin.readline())

for test_case in range(1, T+1):
    N = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    max = a[0]
    min = a[0]
    for i in a:
        if i > max:
            max = i
        elif i < min:
            min = i
    result = max - min
    # print(f'#{test_case} {result}')