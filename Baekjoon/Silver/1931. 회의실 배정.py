# https://www.acmicpc.net/problem/1931
import sys
import heapq
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())

meeting = []

for _ in range(N):
    start, end = map(int, input().split())
    heapq.heappush(meeting, (end, start))

end = 0
answer = 0

for _ in range(N):
    time = heapq.heappop(meeting)
    if time[1] >= end:
        answer += 1
        end = time[0]

print(answer)