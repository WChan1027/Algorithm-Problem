# https://www.acmicpc.net/problem/2638
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())

cheese = [list(map(int, input().split())) for _ in range(N)]
direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

end = 0
cnt = 0
while end == 0:
    air = [[0] * M for _ in range(N)]

    que = [(0, 0)]
    air[0][0] = 1
    while que:
        now_x, now_y = que.pop()
        for dir in direction:
            next_x = now_x + dir[0]
            next_y = now_y + dir[1]
            if 0 <= next_x < N and 0 <= next_y < M:
                if cheese[next_x][next_y] == 0 and air[next_x][next_y] == 0:
                    air[next_x][next_y] = 1
                    que.append((next_x, next_y))
                elif cheese[next_x][next_y] == 1 and air[next_x][next_y] == 0:
                    air[next_x][next_y] = -1
                elif cheese[next_x][next_y] == 1 and air[next_x][next_y] == -1:
                    air[next_x][next_y] = -2

    for i in range(N):
        for j in range(M):
            if air[i][j] == -2:
                cheese[i][j] = 0

    end = 1
    for i in range(N):
        if 1 in cheese[i]:
            end = 0
            break

    cnt += 1

print(cnt)