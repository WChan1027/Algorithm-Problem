# https://www.acmicpc.net/problem/2206
import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())

maze = [list(map(int, input().strip())) for _ in range(N)]

dp = [list([float('inf'), float('inf')] for _ in range(M)) for _ in range(N)]

direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

que = deque()
que.append((0, 0, 0))
dp[0][0] = [1, 1]

while que:
    now_x, now_y, wall = que.popleft()

    if now_x == N-1 and now_y == M-1:
        pass

    else:
        for dir in direction:
            next_x = now_x + dir[0]
            next_y = now_y + dir[1]

            if 0 <= next_x < N and 0 <= next_y < M:
                if maze[next_x][next_y] == 1:
                    if wall == 0:
                        if dp[next_x][next_y][1] > dp[now_x][now_y][0] + 1:
                            if dp[now_x][now_y][0] + 1 < min(dp[N-1][M-1]):
                                dp[next_x][next_y][1] = dp[now_x][now_y][0] + 1
                                que.append((next_x, next_y, 1))

                else:
                    if dp[next_x][next_y][wall] > dp[now_x][now_y][wall] + 1:
                        if dp[now_x][now_y][wall] + 1 < min(dp[N - 1][M - 1]):
                            dp[next_x][next_y][wall] = dp[now_x][now_y][wall] + 1
                            que.append((next_x, next_y, wall))


if min(dp[N-1][M-1]) == float('inf'):
    print(-1)
else:
    print(min(dp[N-1][M-1]))