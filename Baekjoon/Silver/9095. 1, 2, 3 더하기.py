# https://www.acmicpc.net/problem/9095
import sys
sys.stdin = open('input.txt')
T = int(sys.stdin.readline())

for test_case in range(T):
    n = int(sys.stdin.readline())

    num = [0] * (n+1)
    if n == 1:
        print(1)
    elif n == 2:
        print(2)
    elif n == 3:
        print(4)
    else:
        num[1] = 1
        num[2] = 2
        num[3] = 4
        for i in range(4, n+1):
            num[i] = num[i-1] + num[i-2] + num[i-3]
        print(num[n])