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

    print(2*n-1)