https://www.acmicpc.net/problem/4179
import sys
from collections import deque

# 어떤 출구가 있을 때, 지훈이가 출구까지 가는 데 걸리는 시간 < 불이 출구까지 번지는 데 걸리는 시간 이면 탈출 가능

R, C = map(int, sys.stdin.readline().split())

maze = [list(sys.stdin.readline()) for _ in range(R)]       # 미로
fire = []       # 불이 하나가 아닐 수 있으므로 list
# 지훈이의 위치와 불의 위치 저장
for i in range(R):
    for j in range(C):
        if maze[i][j] == 'J':
            jihoon_x, jihoon_y = i, j
        elif maze[i][j] == 'F':
            fire.append([i, j])

direction = [[1, 0], [0, 1], [-1, 0], [0, -1]]
jihoon_goal = {}    # 지훈이와 출구까지의 거리
fire_goal = {}      # 불과 출구까지의 거리

# x, y의 위치에서 출구 까지의 거리를 구하는 함수, BFS
def distance(x, y, goal):
    step = [[0]*C for _ in range(R)]        # 걸리는 시간을 기록하는 리스트
    stack = deque()
    stack.append([x, y])
    while stack:        # 갈 수 있는 길 모두 찾기
        [x, y] = stack.popleft()
        for way in direction:
            next_x, next_y = x + way[0], y + way[1]
            if 0 <= next_x < R and 0 <= next_y < C:     # 아직 미로 내부일 때
                if step[next_x][next_y] == 0 and maze[next_x][next_y] == '.':
                    step[next_x][next_y] = step[x][y] + 1
                    stack.append([next_x, next_y])

            else:       # 출구에 도달했을 때
                if (x, y) in goal:      # 해당 출구까지 도착한 적 있으면 (불이 여러개인 경우 때문에 넣은 조건)
                    if goal[(x, y)] > step[x][y] + 1:       # 이전보다 걸린 시간이 짧으면 출구의 위치, 걸린 시간 저장
                        goal[(x, y)] = step[x][y] + 1
                else:       # 처음 도착하는 출구라면
                    goal[(x, y)] = step[x][y] + 1       # 출구의 위치, 걸린 시간 저장
    return

distance(jihoon_x, jihoon_y, jihoon_goal)       # 지훈이와 출구까지의 거리 구하기
for i in fire:      # 출구에서 모든 불까지의 최단 거리 구하기
    [fire_x, fire_y] = i[0], i[1]
    distance(fire_x, fire_y, fire_goal)

answer = float('INF')

for i in jihoon_goal.keys():        # 어떤 출구까지 지훈이가 걸리는 시간에 대하여
    if jihoon_goal[i] < answer:     # 저장된 값보다 빨리 도착하는 출구라면
        if i in fire_goal:      # 해당 출구에 불이 도달할 수 있을 때
            if jihoon_goal[i] < fire_goal[i]:       # 불보다 빨리 도착하면
                answer = jihoon_goal[i]     # 답으로 저장

        else:       # 불이 도달하지 못하는 출구면
            answer = jihoon_goal[i]     # 답으로 저장

if answer == float('INF'):        # 탈출할 수 없으면
    print('IMPOSSIBLE')     # IMPOSSIBLE 출력
else:       # 탈출 가능하면
    print(answer)       # 최소값 출력