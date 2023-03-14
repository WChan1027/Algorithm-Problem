# https://www.acmicpc.net/problem/14938
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n, m, r = map(int, input().split())

items = list(map(int, input().split()))

road = [[0] * n for _ in range(n)]

for _ in range(r):
    a, b, l = map(int, input().split())
    a -= 1
    b -= 1
    road[a][b] = l
    road[b][a] = l

result = 0

for start in range(n):
    stack = [(start, m)]
    visited = [0] * n
    visited[start] = 1

    get = items[start]

    while stack:
        now, l = stack.pop()

        for next in range(n):
            if road[now][next] != 0 and l >= road[now][next]:
                if visited[next] == 0:
                    get += items[next]
                visited[next] = 1
                stack.append((next, l - road[now][next]))

    result = max(result, get)

print(result)