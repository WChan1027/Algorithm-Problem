import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())

house = [list(map(int, input().split())) for _ in range(N)]

visited = [[0] * N for _ in range(N)]
visited[0][0] = 1
visited[0][1] = 1

answer = 0

# 0: 우향, 1: 우하향, 2: 하향
stack = [(0, 1, 0)]

while stack:
    now_x, now_y, dir = stack.pop()

    if dir == 0:
        next_x = now_x
        next_y = now_y + 1
        next_dir = 0
        if 0 <= next_x < N and 0 <= next_y < N and visited[next_x][next_y] == 0:
            visited[next_x][next_y] = 1
            stack.append((next_x, next_y, next_dir))

        next_x = now_x + 1
        next_y = now_y + 1
        next_dir = 1
        if 0 <= next_x < N and 0 <= next_y < N and visited[next_x][next_y] == 0 and visited[next_x - 1][next_y] == 0 and visited[next_x][next_y - 1]:
            visited[next_x][next_y] = 1
            visited[next_x - 1][next_y] = 1
            visited[next_x][next_y - 1] = 1



    elif dir == 1:

    else: