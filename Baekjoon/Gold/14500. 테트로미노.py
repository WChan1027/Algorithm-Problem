# https://www.acmicpc.net/problem/14500
import sys
sys.stdin = open('input.txt')

N, M = map(int, sys.stdin.readline().split())

paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]

answer = 0
visited = [[0] * M for _ in range(N)]

def move(x, y, result, count):
    global answer
    if count == 4:
        if result > answer:
            answer = result
        return

    for i in range(4):
        next_x = x + direction[i][0]
        next_y = y + direction[i][1]
        if 0 <= next_x < N and 0 <= next_y < M:
            if visited[next_x][next_y] == 0:
                if count == 2:
                    visited[next_x][next_y] = 1
                    move(x, y, result + paper[next_x][next_y], count + 1)
                    visited[next_x][next_y] = 0
                visited[next_x][next_y] = 1
                move(next_x, next_y, result + paper[next_x][next_y], count + 1)
                visited[next_x][next_y] = 0

for i in range(N):
    for j in range(M):
        visited[i][j] = 1
        move(i, j, paper[i][j], 1)
        visited[i][j] = 0

print(answer)