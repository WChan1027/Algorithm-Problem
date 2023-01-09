# https://www.acmicpc.net/problem/2667
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())

houses = [list(map(str, input().strip())) for _ in range(N)]

check = [[0] * N for _ in range(N)]

direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

stack = []
result = []
for i in range(N):
    for j in range(N):
        if houses[i][j] == '1' and check[i][j] == 0:
            stack.append((i, j))
            check[i][j] = 1
            cnt = 1
            while stack:
                x, y = stack.pop()
                for dir in direction:
                    next_x, next_y = x + dir[0], y + dir[1]
                    if 0 <= next_x < N and 0 <= next_y < N:
                        if houses[next_x][next_y] == '1' and check[next_x][next_y] == 0:
                            stack.append((next_x, next_y))
                            check[next_x][next_y] = 1
                            cnt += 1
            result.append(cnt)

result.sort()
print(len(result))

for i in result:
    print(i)