import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

R, C = map(int, input().split())

mine = [list(input().strip()) for _ in range(R)]

direction = [(1, 1), (1, -1), (-1 ,-1), (-1, 1)]

visited = [[0] * C for _ in range(R)]

def CheckSize(s, x, y):
    length = s
    if x + length * 2 >= R or y + length >= C or y - length < 0:
        return 0

    stack = [(x, y, 0)]
    visited[x][y] = 1

    while stack:
        now_x, now_y, d = stack.pop()

        next_x, next_y = now_x + direction[d][0], now_y + direction[d][1]
        if 0 <= next_x < R and 0 <= next_y < C and mine[next_x][next_y] == 1:
            stack.append((next_x, next_y, d))
            visited[next_x][next_y] = 1

# 현재까지의 최대 사이즈 기록.
# visited == 0 인 점들에 대해 CheckSize(현재까지의 최대 사이즈, x, y) 를 통해 사이즈 체크.
# 이 과정에서 지난 점들은 visited 체크. 이 점들은 윗꼭지점이 될 수 없음.

size = 0
for i in range(R):
    for j in range(C):
