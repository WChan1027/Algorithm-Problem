import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

answer = [[-1] * m for _ in range(n)]
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
start_x, start_y = 0, 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            start_x, start_y = i, j
            answer[i][j] = 0
        elif graph[i][j] == 0:
            answer[i][j] = 0

queue = deque()
queue.append((start_x, start_y))

while queue:
    now_x, now_y = queue.popleft()
    for d in direction:
        next_x, next_y = now_x + d[0], now_y + d[1]
        if 0 <= next_x < n and 0 <= next_y < m:
            if graph[next_x][next_y] == 1 and answer[next_x][next_y] == -1:
                answer[next_x][next_y] = answer[now_x][now_y] + 1
                queue.append((next_x, next_y))

for result in answer:
    print(*result)