# https://www.acmicpc.net/problem/2448
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())

stars = [[' '] * (2*N) for _ in range(N)]
for i in range(N):
    for j in range(N-i-1, N+i):
        stars[i][j] = '*'

def star(N, x, y):
    if N == 3:
        stars[x+1][y] = ' '
        return

    for i in range(N//2):
        for j in range(y-i, y+i+1):
            stars[x+N-1-i][j] = ' '

    star(N//2, x, y)
    star(N//2, x+N//2, y-N//2)
    star(N//2, x+N//2, y+N//2)

star(N, 0, N-1)

for answer in stars:
    print(''.join(answer))