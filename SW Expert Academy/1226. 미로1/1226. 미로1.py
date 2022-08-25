import sys
from pprint import pprint
sys.stdin = open('input.txt')

def dfs(sp_x, sp_y):        # dfs
    stack_x = [sp_x]
    stack_y = [sp_y]

    while stack_x:
        cp_x, cp_y = stack_x.pop(), stack_y.pop()

        for i in range(4):
            next_x, next_y = cp_x + direction_x[i], cp_y + direction_y[i]
            if maze[next_x][next_y] == 0 and visited[next_x][next_y] == 0:
                stack_x.append(next_x)
                stack_y.append(next_y)
                visited[next_x][next_y] = visited[cp_x][cp_y] + 1       # visited에 n 저장
            elif maze[next_x][next_y] == 3:     # 도착점 도착 시
                return 1

    return 0        # 도착점에 도착 못했을 시

for test_case in range(1, 11):
    tc = int(input())
    maze = []
    for _ in range(16):
        maze += [list(map(int, input()))]       # 미로 입력

    visited = [[0]*16 for _ in range(16)]       # visited

    for i in range(16):     # 출발지점 확인
        for j in range(16):
            if maze[i][j] == 2:
                sp_x, sp_y = i, j

    direction_x = [1, -1, 0, 0]     # x좌표와 y좌표 분리
    direction_y = [0, 0, 1, -1]
    answer = dfs(sp_x, sp_y)
    pprint(visited)
    print(f'#{tc} {answer}')