# https://www.acmicpc.net/problem/2447
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
stars = list(['*'] * N for _ in range(N))

def star(N, start):
    x, y = start
    if N == 3:
        stars[x+1][y+1] = ' '
        return

    for i in range(N//3):
        for j in range(N//3):
            stars[x+N//3+i][y+N//3+j] = ' '
    star(N//3, [x, y])
    star(N//3, [x+N//3, y])
    star(N//3, [x+2*(N//3), y])
    star(N//3, [x, y+N//3])
    star(N//3, [x+2*(N//3), y+N//3])
    star(N//3, [x, y+2*(N//3)])
    star(N//3, [x+N//3, y+2*(N//3)])
    star(N//3, [x+2*(N//3), y+2*(N//3)])

star(N, [0,0])

for answer in stars:
    print(''.join(answer))