# https://www.acmicpc.net/problem/1730
import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
moves = sys.stdin.readline()

visited = [[1] * N for _ in range(N)]
picture = [[0] * N for _ in range(N)]
index = (0, 0)

for move in moves:
    (x, y) = index
    if move == 'U':
        next_x, next_y = x-1, y
        if 0 <= next_x < N and 0 <= next_y < N:
            visited[x][y] *= 2
            visited[next_x][next_y] *= 2
            index = (next_x, next_y)
    elif move == 'D':
        next_x, next_y = x+1, y
        if 0 <= next_x < N and 0 <= next_y < N:
            visited[x][y] *= 2
            visited[next_x][next_y] *= 2
            index = (next_x, next_y)
    elif move == 'R':
        next_x, next_y = x, y+1
        if 0 <= next_x < N and 0 <= next_y < N:
            visited[x][y] *= 3
            visited[next_x][next_y] *= 3
            index = (next_x, next_y)
    elif move == 'L':
        next_x, next_y = x, y-1
        if 0 <= next_x < N and 0 <= next_y < N:
            visited[x][y] *= 3
            visited[next_x][next_y] *= 3
            index = (next_x, next_y)

for x in range(N):
    for y in range(N):
        if visited[x][y] % 6 == 0:
            picture[x][y] = '+'
        elif visited[x][y] % 3 == 0:
            picture[x][y] = '-'
        elif visited[x][y] % 2 == 0:
            picture[x][y] = '|'
        else:
            picture[x][y] = '.'

for row in picture:
    print(''.join(row))