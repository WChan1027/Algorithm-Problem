# https://www.acmicpc.net/problem/7576

import sys
from collections import deque
sys.stdin = open('input.txt')

M, N = map(int, sys.stdin.readline().split())

tomato = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

visited = [[-1]*M for _ in range(N)]
stack = deque()
unripe = 0
for m in range(M):
    for n in range(N):
        if tomato[n][m] == 1:
            stack.append((n, m))
            visited[n][m] = 0

        elif tomato[n][m] == -1:
            visited[n][m] = 1

        else:
            unripe += 1

direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

if unripe == 0:
    print(0)

else:
    count = 0
    while stack:
        ripe_y, ripe_x = stack.popleft()
        for i in range(4):
            next_ripe_x = ripe_x + direction[i][0]
            next_ripe_y = ripe_y + direction[i][1]
            if 0 <= next_ripe_x < M and 0 <= next_ripe_y < N:
                if visited[next_ripe_y][next_ripe_x] == -1:
                    stack.append((next_ripe_y, next_ripe_x))
                    visited[next_ripe_y][next_ripe_x] = visited[ripe_y][ripe_x] + 1
                    count += 1

    if count == unripe:
        print(visited[ripe_y][ripe_x])

    else:
        print(-1)