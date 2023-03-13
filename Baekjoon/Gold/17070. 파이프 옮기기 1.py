import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())

house = [list(map(int, input().split())) for _ in range(N)]

num = [[0] * N for _ in range(N)]


answer = 0

# 0: 우향, 1: 우하향, 2: 하향

def pipe(x, y, d):
    global answer, N


    if x == N-1 and y == N-1:
        answer += 1
        return


    if d == 0:
        next_x = x
        next_y = y + 1
        if 0 <= next_x < N and 0 <= next_y < N and house[next_x][next_y] == 0:
            pipe(next_x, next_y, 0)

        next_x = x + 1
        next_y = y + 1
        if 0 <= next_x < N and 0 <= next_y < N and house[next_x][next_y] == 0 and house[next_x - 1][next_y] == 0 and house[next_x][next_y - 1] == 0:
            pipe(next_x, next_y, 1)


    elif d == 1:
        next_x = x
        next_y = y + 1
        if 0 <= next_x < N and 0 <= next_y < N and house[next_x][next_y] == 0:
            pipe(next_x, next_y, 0)

        next_x = x + 1
        next_y = y + 1
        if 0 <= next_x < N and 0 <= next_y < N and house[next_x][next_y] == 0 and house[next_x - 1][next_y] == 0 and house[next_x][next_y - 1] == 0:
            pipe(next_x, next_y, 1)

        next_x = x + 1
        next_y = y
        if 0 <= next_x < N and 0 <= next_y < N and house[next_x][next_y] == 0:
            pipe(next_x, next_y, 2)


    else:
        next_x = x + 1
        next_y = y + 1
        if 0 <= next_x < N and 0 <= next_y < N and house[next_x][next_y] == 0 and house[next_x - 1][next_y] == 0 and house[next_x][next_y - 1] == 0:
            pipe(next_x, next_y, 1)

        next_x = x + 1
        next_y = y
        if 0 <= next_x < N and 0 <= next_y < N and house[next_x][next_y] == 0:
            pipe(next_x, next_y, 2)

pipe(0, 1, 0)

print(answer)