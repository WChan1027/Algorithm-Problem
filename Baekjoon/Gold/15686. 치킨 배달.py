# https://www.acmicpc.net/problem/15686
import sys
from itertools import combinations
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())

city = [list(map(int, input().split())) for _ in range(N)]

houses = []
chicken = []

for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            houses.append((i, j))
        elif city[i][j] == 2:
            chicken.append((i, j))

answer = float('inf')
for case in combinations(chicken, M):
    total = 0
    for x1, y1 in houses:
        distance = float('inf')
        for x2, y2 in case:
            distance = min(distance, abs(x1 - x2) + abs(y1 - y2))
        total += distance

    answer = min(answer, total)

print(answer)