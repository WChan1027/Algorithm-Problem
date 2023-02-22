# https://www.acmicpc.net/problem/1011
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

T = int(input())

for test_case in range(T):
    x, y = map(int, input().split())

    length = (y - x)

    n = 0
    while n*(n+1) < length:
        n += 1

    n -= 1

    if n*(n+1) == length:
        n *= 2
    elif (n+1)*(n+1) >= length:
        n = 2*n +1
    else:
        n = 2*n +2

    print(n)