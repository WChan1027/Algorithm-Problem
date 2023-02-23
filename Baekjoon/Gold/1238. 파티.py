# https://www.acmicpc.net/problem/1238
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M, X = map(int, input().split())

road = [[0] * (N+1) for _ in range(N+1)]
road_reverse = [[0] * (N+1) for _ in range(N+1)]

for _ in range(M):
    S, E, T = map(int, input().split())
    road[S][E] = T
    road_reverse[E][S] = T


stack = [X]
visited = [100000000] * (N+1)
while stack:
    now = stack.pop()
    visited[X] = 0
    for next in range(1, N + 1):
        if road_reverse[now][next] != 0:
            if visited[next] > visited[now] + road_reverse[now][next] or visited[next] == 0:
                visited[next] = visited[now] + road_reverse[now][next]
                stack.append(next)

stack = [X]
visited_N = [100000000] * (N+1)
while stack:
    now = stack.pop()
    visited_N[X] = 0
    for next in range(1, N + 1):
        if road[now][next] != 0:
            if visited_N[next] > visited_N[now] + road[now][next] or visited_N[next] == 0:
                visited_N[next] = visited_N[now] + road[now][next]
                stack.append(next)

total = [0] * N
for i in range(1, N+1):
    total[i-1] = visited[i] + visited_N[i]

print(max(total))