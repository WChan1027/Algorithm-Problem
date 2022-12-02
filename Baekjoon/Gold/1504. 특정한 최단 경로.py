# https://www.acmicpc.net/problem/1504
import sys
sys.stdin = open('input.txt')

N, E = map(int, sys.stdin.readline().split())

road = [[0 for _ in range(N+1)] for _ in range(N+1)]        # 정점끼리 간선이 표시된 그래프
length = [[0 for _ in range(N+1)] for _ in range(N+1)]      # 정점끼리 간선의 길이


for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    road[a][b] = 1
    road[b][a] = 1
    length[a][b] = c
    length[b][a] = c

v1, v2 = map(int, sys.stdin.readline().split())

# min_distance = 1000 * E
# result = []
# answer = 0
#
# def find_path(now, goal, path, distance):
#     global min_distance, v1, v2
#     if now == goal:
#         if min_distance > distance:
#             min_distance = distance
#             if v1 in path and v2 in path:
#                 result.append(distance)
#         return
#
#     for i in range(1, N+1):
#         if road[now][i] == 1 and visited[i] == 0 and distance + length[now][i] < min_distance:
#             visited[i] = 1
#             find_path(i, goal, path + [i], distance + length[now][i])
#             visited[i] = 0
#
#     return
#
# find_path(1, N, [1], 0)
#
# if result:
#     print(min(result))
# else:
#     print(-1)

from collections import deque

def distance(now, goal):
    global error
    visited = [1000 * E for _ in range(N + 1)]
    visit = [0 for _ in range(N + 1)]
    stack = deque()
    stack.append(now)

    visited[now] = 0

    while stack:
        n = stack.popleft()
        for i in range(1, N+1):
            if road[n][i] == 1 and visited[i] >= (visited[n] + length[n][i]):
                stack.append(i)
                visit[i] = 1
                visited[i] = visited[n] + length[n][i]

    if visit[goal] == 0:
        error = 1

    return visited[goal]


error = 0
if v1 == 1 and v2 != N:
    answer = distance(1, v2) + distance(v2, N)
elif v1 != 1 and v2 == N:
    answer = distance(1, v1) + distance(v1, N)
elif v1 == 1 and v2 == N:
    answer = distance(1, N)
else:
    answer = min((distance(1, v1) + distance(v1, v2) + distance(v2, N)), (distance(1, v2) + distance(v2, v1) + distance(v1, N)))

if error == 1:
    print(-1)
else:
    print(answer)