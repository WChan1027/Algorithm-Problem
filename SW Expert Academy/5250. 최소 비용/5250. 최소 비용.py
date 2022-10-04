import sys
sys.stdin = open('sample_input.txt')
from collections import deque

# def BFS(x, y):
#     if x == N-1 and y == N-1:       # 도착하면 종료
#         return
#
#     for i in range(4):      # 상하좌우 방향에 대해 실행
#         next_x = x + direction[i][1]
#         next_y = y + direction[i][0]
#         if 0 <= next_x < N and 0 <= next_y < N:     # 다음 지점이 범위 내라면
#             # 다음 지점까지 소모되는 연료
#             if height[next_x][next_y] > height[x][y]:
#                 next_fuel = fuel[x][y] + height[next_x][next_y] - height[x][y] + 1
#             else:
#                 next_fuel = fuel[x][y] + 1
#
#             if (next_x + next_y) != 0 and fuel[next_x][next_y] == 0:        # 다음 지점이 출발점이 아니고, 간 적 없으면
#                 fuel[next_x][next_y] = next_fuel      # 소모되는 연료 저장
#                 BFS(next_x, next_y)     # 다음 지점으로 이동
#             elif fuel[next_x][next_y] != 0:     # 다음 지점에 간 적 있으면
#                 if fuel[next_x][next_y] > next_fuel:      # 지금의 경로가 최소비용이면
#                     fuel[next_x][next_y] = next_fuel      # 소모되는 연료 저장
#                     BFS(next_x, next_y)     # 다음 지점으로 이동
#     return

def BFS(x, y):
    stack = deque()
    stack.append([x, y])

    while stack:
        [x, y] = stack.popleft()
        for i in range(4):      # 상하좌우에 대해 이동했을 때
            next_x = x + direction[i][1]
            next_y = y + direction[i][0]
            if 0 <= next_x < N and 0 <= next_y < N:     # 범위 내라면
                if height[next_x][next_y] > height[x][y]:       # 더 높은 곳으로 이동하는 경우 연료 소모
                    next_fuel = fuel[x][y] + height[next_x][next_y] - height[x][y] + 1
                else:
                    next_fuel = fuel[x][y] + 1      # 그렇지 않을 경우 연료 소모
                if (next_x + next_y) != 0 and fuel[next_x][next_y] == 0:        # 이동 지역이 출발지점이 아니고 처음 가는 곳일 경우
                    fuel[next_x][next_y] = next_fuel        # 연료 소모값 저장
                    stack.append([next_x, next_y])      # 이동 지역 stack에 추가
                elif fuel[next_x][next_y] != 0:     # 가본 적 있는 경우
                    if fuel[next_x][next_y] > next_fuel:        # 현재 경로의 연료 소모값이 더 작을 때
                        fuel[next_x][next_y] = next_fuel        # 연료 소모값 저장
                        stack.append([next_x, next_y])      # 이동 지역 stack에 추가

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    height = [list(map(int, input().split())) for _ in range(N)]

    fuel = [[0]*N for _ in range(N)]
    direction = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    BFS(0, 0)

    print(f'#{test_case} {fuel[N-1][N-1]}')