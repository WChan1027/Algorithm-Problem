import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline

R, C = map(int, input().split())

mine = [list(map(int, input().strip())) for _ in range(R)]

direction = [(1, 1), (1, -1), (-1, -1), (-1, 1)]

def CheckSize(s, x, y):
    if x + s * 2 >= R or y + s >= C or y - s < 0:
        return 1

    result = 1
    que = deque()
    que.append((x, y, 0, 0))
    while que:
        now_x, now_y, d, cnt = que.pop()
        # print(que)
        # print('now : ', now_x, now_y, d, cnt)
        if d == 0:
            next_x, next_y = now_x + direction[d][0], now_y + direction[d][1]
            if 0 <= next_x < R and 0 <= next_y < C and mine[next_x][next_y] == 1:
                # print('우하향', next_x, next_y, cnt)
                que.append((next_x, next_y, d, cnt + 1))

            if cnt >= s and cnt > 0:
                next_x, next_y = now_x + direction[d+1][0], now_y + direction[d+1][1]
                if 0 <= next_x < R and 0 <= next_y < C and mine[next_x][next_y] == 1:
                    # print('좌하향 선회', next_x, next_y, cnt)
                    que.append((next_x, next_y, d+1, cnt))

        elif d == 1:
            if now_y == y:
                next_x, next_y = now_x + direction[d+1][0], now_y + direction[d+1][1]
                if 0 <= next_x < R and 0 <= next_y < C and mine[next_x][next_y] == 1:
                    # print('좌상향 선회', next_x, next_y, cnt)
                    que.append((next_x, next_y, d+1, cnt))
            else:
                next_x, next_y = now_x + direction[d][0], now_y + direction[d][1]
                if 0 <= next_x < R and 0 <= next_y < C and mine[next_x][next_y] == 1:
                    # print('좌하향', next_x, next_y, cnt)
                    que.append((next_x, next_y, d, cnt))

        elif d == 2:
            if now_x == x + cnt:
                next_x, next_y = now_x + direction[d+1][0], now_y + direction[d+1][1]
                if 0 <= next_x < R and 0 <= next_y < C and mine[next_x][next_y] == 1:
                    # print('우상향 선회', next_x, next_y, cnt)
                    que.append((next_x, next_y, d+1, cnt))
            else:
                next_x, next_y = now_x + direction[d][0], now_y + direction[d][1]
                if 0 <= next_x < R and 0 <= next_y < C and mine[next_x][next_y] == 1:
                    # print('좌상향', next_x, next_y, cnt)
                    que.append((next_x, next_y, d, cnt))
        elif d == 3:
            if now_y == y and now_x == x:
                if result < cnt + 1:
                    # print('도착', x, y, cnt+1)
                    result = cnt + 1
            else:
                next_x, next_y = now_x + direction[d][0], now_y + direction[d][1]
                if 0 <= next_x < R and 0 <= next_y < C and mine[next_x][next_y] == 1:
                    # print('우상향', next_x, next_y, cnt)
                    que.append((next_x, next_y, d, cnt))
    return result

size = 0
for i in range(R):
    for j in range(C):
        if mine[i][j] == 1:
            size = max(size, CheckSize(size, i, j))

print(size)