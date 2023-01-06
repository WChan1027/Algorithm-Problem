# https://www.acmicpc.net/problem/1927
import sys
import heapq
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())

heap = []

for _ in range(N):
    x = int(input())
    if x == 0:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, x)