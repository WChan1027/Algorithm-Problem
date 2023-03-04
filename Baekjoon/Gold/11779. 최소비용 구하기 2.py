# https://www.acmicpc.net/problem/11779
import sys
from collections import defaultdict
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
m = int(input())

city = defaultdict(list)
visited = [float('inf')] * (n+1)
route = [0] * (n+1)

for _ in range(m):
    s, e, v = map(int, input().split())

    city[s].append((e, v))

S, E = map(int, input().split())

stack = [(S, 0)]
visited[S] = 0

while stack:
    now, spend = stack.pop()
    if spend <= visited[now]:
        if visited[now] <= visited[E]:
            for bus in city[now]:
                next = bus[0]
                price = bus[1]

                if visited[next] > visited[now] + price:
                    visited[next] = visited[now] + price
                    route[next] = now
                    stack.append((next, visited[next]))

path = [E]

while S not in path:
    now = path[0]
    path.insert(0, route[now])

print(visited[E])
print(len(path))
print(*path)
