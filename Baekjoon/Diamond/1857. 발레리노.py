# https://www.acmicpc.net/problem/1857
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

m, n = map(int, input().split())

floor = [list(map(int, input().split())) for _ in range(m)]

for i in range(m):
    for j in range(n):
        if floor[i][j] == 3:
            start = (i, j, 0)
        elif floor[i][j] == 4:
            end = (i, j, 0)

visited = [[float('inf')] * n for _ in range(m)]
direction = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
visited[start[0]][start[1]] = 0
stack = [start]
case = 0

while stack:
    now_x, now_y, cnt = stack.pop()

    if visited[end[0]][end[1]] <= visited[now_x][now_y]:
        continue

    else:
        for dir in direction:
            next_x = now_x + dir[0]
            next_y = now_y + dir[1]

            if 0 <= next_x < m and 0 <= next_y < n:
                if floor[next_x][next_y] == 4:
                    if visited[end[0]][end[1]] > visited[now_x][now_y] + 1:
                        visited[end[0]][end[1]] = visited[now_x][now_y] + 1
                        case = 1
                    elif visited[end[0]][end[1]] == visited[now_x][now_y] + 1:
                        case += 1

                elif floor[next_x][next_y] == 1:
                    if visited[next_x][next_y] > visited[now_x][now_y]:
                        visited[next_x][next_y] = visited[now_x][now_y]
                        stack.append((next_x, next_y, cnt + 1))
                    elif visited[next_x][next_y] == visited[now_x][now_y]:
                        

                elif floor[next_x][next_y] == 0:
                    if visited[next_x][next_y] >= visited[now_x][now_y] + 1:
                        visited[next_x][next_y] = visited[now_x][now_y] + 1
                        stack.append((next_x, next_y, cnt))

if visited[end[0]][end[1]] == float('inf'):
    print(-1)
else:
    print(visited[end[0]][end[1]] - 1)

print(case)