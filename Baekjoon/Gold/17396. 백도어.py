# https://www.acmicpc.net/problem/17396
import sys
import heapq
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
vision = list(map(int, input().split()))
vision[-1] = 0
checkpoint = [[] for _ in range(N)]

for _ in range(M):
    a, b, t = map(int, input().split())

    checkpoint[a].append([b, t])
    checkpoint[b].append([a, t])


result = [float('INF')] * N
result[0] = 0
visited = [0] * N

def dijkstra():
    que = []
    heapq.heappush(que, (0, 0))

    while que:
        now, distance = heapq.heappop(que)
        if distance > result[now]:
            continue

        for next in checkpoint[now]:
            if result[next[0]] > result[now] + next[1] and vision[next[0]] == 0:
                result[next[0]] = result[now] + next[1]
                heapq.heappush(que, (next[0], result[next[0]]))

    return

dijkstra()

if result[-1] == float('INF'):
    print(-1)
else:
    print(result[-1])