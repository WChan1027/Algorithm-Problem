import sys
from collections import defaultdict
import heapq
sys.stdin = open('input.txt')
input = sys.stdin.readline

V, E = map(int, input().split())

K = int(input())

route = defaultdict(list)

for _ in range(E):
    u, v, w = map(int, input().split())
    route[u].append((v, w))

length = [float('INF')] * (V+1)
length[K] = 0

que = []
heapq.heappush(que, (0, K))

while que:
    distance, now = heapq.heappop(que)

    if length[now] >= distance:
        for next, value in route[now]:
            if distance + value < length[next]:
                length[next] = distance + value
                heapq.heappush(que, (distance + value, next))


for answer in length[1:]:
    if answer == float('inf'):
        print('INF')
    else:
        print(answer)