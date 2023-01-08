# https://www.acmicpc.net/problem/6064
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

T = int(input())

for test_case in range(1, T+1):
    M, N, x, y = map(int, input().split())

    mp = 0

    while True:
        if (M * mp + x - y) % N == 0:
            print(M * mp + x)
            break
        mp += 1
        if (M * mp) % N == 0:
            print(-1)
            break