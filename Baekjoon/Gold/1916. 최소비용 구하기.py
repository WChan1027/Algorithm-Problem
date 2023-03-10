# https://www.acmicpc.net/problem/1916
import sys
from collections import defaultdict
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
M = int(input())
road = defaultdict(list)

for _ in range(M):
    S, E, V = map(int, input().split())
    road[S] += [(E, V)]

S, E = map(int, input().split())
stack = [S]
visited = [-1] * (N+1)
visited[S] = 0

while stack:
    now = stack.pop()

    for route in road[now]:
        next, value = route

        if visited[next] == -1:
            visited[next] = visited[now] + value
            stack.append(next)

        elif visited[now] + value < visited[next]:
            visited[next] = visited[now] + value

            if visited[E] != -1:
                stack.append(next)

            else:
                if visited[next] < visited[E]:
                    stack.append(next)

print(visited)