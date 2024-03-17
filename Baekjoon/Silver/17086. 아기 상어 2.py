import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())

space = [list(map(int, input().split())) for _ in range(N)]

sharks = []

for i in range(N):
    for j in range(M):
        if space[i][j] == 1:
            sharks.append((i, j))

visited = [[0] * M for _ in range(N)]
direction = [(1, 0), (1, 1), (1, -1), (0, 1), (0, -1), (-1, 0), (-1, 1), (-1, -1)]

while sharks:
    now_x, now_y = sharks.pop()

    for dir in direction:
        next_x, next_y = now_x + dir[0], now_y + dir[1]

        if 0 <= next_x < N and 0 <= next_y < M:
            if space[next_x][next_y] == 0:
                if visited[next_x][next_y] == 0:
                    visited[next_x][next_y] = visited[now_x][now_y] + 1
                    sharks.append((next_x, next_y))
                elif visited[next_x][next_y] > visited[now_x][now_y] + 1:
                    visited[next_x][next_y] = visited[now_x][now_y] + 1
                    sharks.append((next_x, next_y))

answer = 0
for i in range(N):
    for j in range(M):
        answer = max(answer, visited[i][j])

print(answer)