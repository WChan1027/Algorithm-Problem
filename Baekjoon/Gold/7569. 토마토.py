# https://www.acmicpc.net/problem/7569

import sys
from collections import deque
sys.stdin = open('input.txt')

M, N, H = map(int, sys.stdin.readline().split())

tomato = []

for _ in range(H):
    layer = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    tomato.append(layer)

visited = [[[-1]*M for _ in range(N)] for _ in range(H)]
stack = deque()
unripe = 0
for h in range(H):
    for n in range(N):
        for m in range(M):
            if tomato[h][n][m] == 1:
                stack.append((h, n, m))
                visited[h][n][m] = 0

            elif tomato[h][n][m] == -1:
                visited[h][n][m] = 1

            else:
                unripe += 1

direction = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]

if unripe == 0:
    print(0)

else:
    count = 0
    while stack:
        ripe_z, ripe_y, ripe_x = stack.popleft()
        for i in range(6):
            next_ripe_z = ripe_z + direction[i][0]
            next_ripe_y = ripe_y + direction[i][1]
            next_ripe_x = ripe_x + direction[i][2]
            if 0 <= next_ripe_z < H and 0 <= next_ripe_y < N and 0 <= next_ripe_x < M:
                if visited[next_ripe_z][next_ripe_y][next_ripe_x] == -1:
                    stack.append((next_ripe_z, next_ripe_y, next_ripe_x))
                    visited[next_ripe_z][next_ripe_y][next_ripe_x] = visited[ripe_z][ripe_y][ripe_x] + 1
                    count += 1

    if count == unripe:
        print(visited[ripe_z][ripe_y][ripe_x])

    else:
        print(-1)