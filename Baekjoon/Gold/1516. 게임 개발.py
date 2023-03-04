# https://www.acmicpc.net/problem/1516
import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())

cnt = [0]*(N+1)
graph = [[]for _ in range(N+1)]
time = [0]*(N+1)

for i in range(1, N+1):
    building = list(map(int, input().split()))
    time[i] = building[0]
    for j in building[1:]:
        if j == -1:
            break
        else:
            graph[i].append(j)
            cnt[i] += 1

queue = deque()
for i in range(1, N+1):
    if cnt[i] == 0:
        queue.append(i)

while queue:
    now = queue.popleft()
    t = 0

    for next in range(1, N+1):
        if now in graph[next]:
            cnt[next] -= 1
            if cnt[next] == 0:
                queue.append(next)
        if next in graph[now]:
            t = max(time[next], t)

    time[now] += t

for i in time[1:]:
    print(i)