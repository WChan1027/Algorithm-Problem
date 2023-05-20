# https://www.acmicpc.net/problem/7576
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque

M, N = map(int, input().split())

tomato = [list(map(int, input().split())) for _ in range(N)]

visited = [[-1] * M for _ in range(N)]  # 토마토가 익었는지 확인하기 위한 리스트
direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
que = deque()

unripe = 0                              # 익지 않은 토마토 수
for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:           # 익은 토마토
            visited[i][j] = 0           # 익은 날짜 : 0일차
            que.append((i, j))          # 익은 토마토 위치 기록

        elif tomato[i][j] == -1:        # 빈 칸
            visited[i][j] = -2

        else:                           # 익지 않은 토마토
            unripe += 1                 # 익지 않은 토마토 +1

if unripe == 0:                         # 익지 않은 토마토가 없으면
    print(0)                            # 0 출력

else:                                   # 익지 않은 토마토가 있으면
    cnt = 0                             # 새로 익는 토마토 수
    while que:
        now_x, now_y = que.popleft()    # 현재 토마토 위치
        for dir in direction:
            next_x = now_x + dir[0]
            next_y = now_y + dir[1]
            if 0 <= next_x < N and 0 <= next_y < M:
                if visited[next_x][next_y] == -1:
                    que.append((next_x, next_y))                            # 새로 익은 토마토 위치 기록
                    visited[next_x][next_y] = visited[now_x][now_y] + 1     # 토마토가 익은 날짜 기록
                    cnt += 1                                                # 새로 익은 토마토 +1

    if cnt == unripe:                                                       # 토마토가 모두 익었으면
        print(visited[now_x][now_y])                                        # 마지막으로 토마토가 익은 날짜 출력

    else:                                                                   # 익지 않은 토마토가 있으면
        print(-1)                                                           # -1 출력