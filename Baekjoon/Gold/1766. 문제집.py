# https://www.acmicpc.net/problem/1766
import sys
from collections import defaultdict
import heapq
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())

solve = defaultdict(list)
cnt = [0] * (N+1)
turn = []

for _ in range(M):
    A, B = map(int, input().split())
    solve[A].append(B)
    cnt[B] += 1

queue = []
turn = []
for i in range(1, N+1):
    if cnt[i] == 0:
        heapq.heappush(queue, i)

while queue:
    now = heapq.heappop(queue)
    turn.append(now)

    for next in solve[now]:
        cnt[next] -= 1

        if cnt[next] == 0:
            heapq.heappush(queue, next)

print(*turn)