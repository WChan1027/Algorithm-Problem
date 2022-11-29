# https://www.acmicpc.net/problem/11724
import sys
from collections import deque
sys.stdin = open('input.txt')

N, M = map(int, sys.stdin.readline().split())

graph = [[0]*N for _ in range(N)]
for _ in range(M):
    s, e = map(int, sys.stdin.readline().split())
    graph[s-1][e-1] = 1
    graph[e-1][s-1] = 1

visited = [0]*N

stack = deque()
count = 0
for i in range(N):
    if visited[i] == 0:
        stack.append(i)
        visited[i] = 1
        count += 1
    while stack:
        a = stack.pop()
        for j in range(N):
            if graph[a][j] == 1 and visited[j] == 0:
                stack.append(j)
                visited[j] = 1

print(count)