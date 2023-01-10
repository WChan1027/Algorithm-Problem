# https://www.acmicpc.net/problem/2178
import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())

maze = [list(map(str, input().strip())) for _ in range(N)]

visited = [[N*M] * M for _ in range(N)]

direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

que = deque()
que.append((0, 0))
visited[0][0] = 1

while que:
    x, y = que.pop()
    for dir in direction:
        next_x, next_y = x + dir[0], y + dir[1]
        if 0 <= next_x < N and 0 <= next_y < M:
            if maze[next_x][next_y] == '1' and visited[next_x][next_y] > visited[x][y] + 1:
                que.append((next_x, next_y))
                visited[next_x][next_y] = visited[x][y] + 1

print(visited[N-1][M-1])