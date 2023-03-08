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

