# https://www.acmicpc.net/problem/11404
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())

m = int(input())

result = [[float('INF')] * n for _ in range(n)]

for _ in range(m):
    start, end, value = map(int, input().split())
    if result[start-1][end-1] > value:
        result[start-1][end-1] = value

for i in range(n):
    result[i][i] = 0

for i in range(n):
    for j in range(n):
        for k in range(n):
            result[j][k] = min(result[j][k], result[j][i] + result[i][k])

for i in range(n):
    for j in range(n):
        if result[i][j] == float('INF'):
            result[i][j] = 0

for a in result:
    print(*a)