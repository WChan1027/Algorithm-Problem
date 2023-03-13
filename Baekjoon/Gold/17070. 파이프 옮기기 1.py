import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())

house = [list(map(int, input().split())) for _ in range(N)]

visited = [[0] * N for _ in range(N)]
visited[0][0] = 1
visited[0][1] = 1

for i in range(N):
    for j in range(N):
        if house[i][j] == 1:
            visited[i][j] = 1

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
        if 0 <= next_x < N and 0 <= next_y < N and visited[next_x][next_y] == 0:
            visited[next_x][next_y] = 1
            pipe(next_x, next_y, 0)
            visited[next_x][next_y] = 0

        next_x = x + 1
        next_y = y + 1
        if 0 <= next_x < N and 0 <= next_y < N and visited[next_x][next_y] == 0 and visited[next_x - 1][next_y] == 0 and visited[next_x][next_y - 1] == 0:
            visited[next_x][next_y] = 1
            visited[next_x - 1][next_y] = 1
            visited[next_x][next_y - 1] = 1
            pipe(next_x, next_y, 1)
            visited[next_x][next_y] = 0
            visited[next_x - 1][next_y] = 0
            visited[next_x][next_y - 1] = 0

    elif d == 1:
        next_x = x
        next_y = y + 1
        if 0 <= next_x < N and 0 <= next_y < N and visited[next_x][next_y] == 0:
            visited[next_x][next_y] = 1
            pipe(next_x, next_y, 0)
            visited[next_x][next_y] = 0

        next_x = x + 1
        next_y = y + 1
        if 0 <= next_x < N and 0 <= next_y < N and visited[next_x][next_y] == 0 and visited[next_x - 1][next_y] == 0 and visited[next_x][next_y - 1] == 0:
            visited[next_x][next_y] = 1
            visited[next_x - 1][next_y] = 1
            visited[next_x][next_y - 1] = 1
            pipe(next_x, next_y, 1)
            visited[next_x][next_y] = 0
            visited[next_x - 1][next_y] = 0
            visited[next_x][next_y - 1] = 0

        next_x = x + 1
        next_y = y
        if 0 <= next_x < N and 0 <= next_y < N and visited[next_x][next_y] == 0:
            visited[next_x][next_y] = 1
            pipe(next_x, next_y, 2)
            visited[next_x][next_y] = 0

    else:
        next_x = x + 1
        next_y = y + 1
        if 0 <= next_x < N and 0 <= next_y < N and visited[next_x][next_y] == 0 and visited[next_x - 1][next_y] == 0 and \
                visited[next_x][next_y - 1] == 0:
            visited[next_x][next_y] = 1
            visited[next_x - 1][next_y] = 1
            visited[next_x][next_y - 1] = 1
            pipe(next_x, next_y, 1)
            visited[next_x][next_y] = 0
            visited[next_x - 1][next_y] = 0
            visited[next_x][next_y - 1] = 0

        next_x = x + 1
        next_y = y
        if 0 <= next_x < N and 0 <= next_y < N and visited[next_x][next_y] == 0:
            visited[next_x][next_y] = 1
            pipe(next_x, next_y, 2)
            visited[next_x][next_y] = 0

pipe(0, 1, 0)

print(answer)