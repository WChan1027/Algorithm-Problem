# https://www.acmicpc.net/problem/14615
import sys
from collections import deque
sys.stdin = open('input.txt')

N, M = map(int, sys.stdin.readline().split())

tube = [[0] * (N+1) for _ in range(N+1)]

for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    tube[x][y] = 1

# tube = [[] for _ in range(N+1)]
#
# for _ in range(M):
#     x, y = map(int, sys.stdin.readline().split())
#     tube[x].append(y)

T = int(sys.stdin.readline())

for test_case in range(T):
    bomb = int(sys.stdin.readline())

    queue = deque()
    queue.append(1)

    visited = [0] * (N+1)
    visited[1] = 1

    complete = 0
    while queue:
        now = queue.popleft()
        if tube[now][bomb] == 1:
            complete = 1
            break
        for next in range(N+1):
            if tube[now][next] == 1 and visited[next] == 0:
                visited[next] = 1
                queue.append(next)


    if complete == 1:

        queue = deque()
        queue.append(bomb)

        visited = [0] * (N + 1)
        visited[bomb] = 1

        while queue:
            now = queue.popleft()
            if tube[now][N] == 1:
                complete = 2
                break
            for next in range(N+1):
                if tube[now][next] == 1 and visited[next] == 0:
                    visited[next] = 1
                    queue.append(next)

    if complete == 2:
        print('Defend the CTP')
    else:
        print('Destroyed the CTP')




# for test_case in range(T):
#     bomb = int(sys.stdin.readline())
#
#     que = deque()
#     que.append(1)
#
#     visited = [0] * (N+1)
#     visited[1] = 1
#
#     complete = 0
#     end = 0
#     while que:
#         now = que.popleft()
#         for next in tube[now]:
#             if next == bomb:
#                 complete = 1
#                 end = 1
#                 break
#             if visited[next] == 0:
#                 visited[next] = 1
#                 que.append(next)
#         if end == 1:
#             break
#
#     if complete == 1:
#         que = deque()
#         que.append(bomb)
#
#         visited = [0] * (N+1)
#         visited[bomb] = 1
#
#         while que:
#             now = que.popleft()
#             if N in tube[now]:
#                 complete = 2
#                 break
#             for next in tube[now]:
#                 if next == N:
#                     complete = 2
#                     end = 2
#                     break
#                 if visited[next] == 0:
#                     visited[next] = 1
#                     que.append(next)
#             if end == 2:
#                 break
#
#     if complete == 2:
#         print('Defend the CTP')
#     else:
#         print('Destroyed the CTP')



# for test_case in range(T):
#     bomb = int(sys.stdin.readline())
#
#     que = deque()
#     que.append(1)
#
#     visited = [0] * (N+1)
#     visited[1] = 1
#
#     complete = 0
#     while que:
#         now = que.pop()
#         if tube[now][bomb] == 1:
#             complete = 1
#             break
#         for next in range(1, N+1):
#             if tube[now][next] == 1 and visited[next] == 0:
#                 visited[next] = 1
#                 que.append(next)
#
#     if complete == 1:
#         que = deque()
#         que.append(bomb)
#
#         visited = [0] * (N+1)
#         visited[bomb] = 1
#
#         while que:
#             now = que.pop()
#             if tube[now][N] == 1:
#                 complete = 2
#                 break
#             for next in range(1, N+1):
#                 if tube[now][next] == 1 and visited[next] == 0:
#                     visited[next] = 1
#                     que.append(next)
#
#     if complete == 2:
#         print('Defend the CTP')
#     else:
#         print('Destroyed the CTP')


# for test_case in range(T):
#     bomb = int(sys.stdin.readline())
#
#     que = [0] * (N+1)
#     que[1] = 1
#
#     visited = [0] * (N+1)
#
#     complete = 0
#     end = 0
#     while end == 0:
#         if que[bomb] == 1:
#             complete = 1
#             break
#         end = 1
#         for now in range(1, N+1):
#             if visited[now] == 0 and que[now] == 1:
#                 end = 0
#                 visited[now] = 1
#                 for next in range(1, N+1):
#                     if tube[now][next] == 1:
#                         que[next] = 1
#
#
#     if complete == 1:
#         que = [0] * (N + 1)
#         que[bomb] = 1
#
#         visited = [0] * (N+1)
#
#         end = 0
#         while end == 0:
#             if que[N] == 1:
#                 complete = 2
#                 break
#             end = 1
#             for now in range(1, N + 1):
#                 if visited[now] == 0 and que[now] == 1:
#                     end = 0
#                     visited[now] = 1
#                     for next in range(1, N + 1):
#                         if tube[now][next] == 1:
#                             que[next] = 1
#
#     if complete == 2:
#         print('Defend the CTP')
#     else:
#         print('Destroyed the CTP')



# def bfs(now, goal):
#     que = deque()
#     que.append(now)
#
#     visited = [0] * (N+1)
#     visited[now] = 1
#
#     while que:
#         a = que.pop()
#         if tube[a][goal] == 1:
#             return 1
#
#         for next in range(1, N+1):
#             if tube[a][next] == 1 and visited[next] == 0:
#                 visited[next] = 1
#                 que.append(next)
#
#     return 0
#
# for test_case in range(T):
#     bomb = int(sys.stdin.readline())
#
#     end = 0
#     if bfs(1, bomb) == 1:
#         if bfs(bomb, N) == 1:
#             print('Defend the CTP')
#             end = 1
#
#     if end == 0:
#         print('Destroyed the CTP')