import sys
import heapq
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())

heap = []

for _ in range(N):
    x = int(input())
    heapq.heappush(heap, (-x, x)) if x else print(heapq.heappop(heap)[1]) if heap else print(0)