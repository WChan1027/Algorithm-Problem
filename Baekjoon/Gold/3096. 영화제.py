# https://www.acmicpc.net/problem/3096
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())

connect = list([] for _ in range(N+1))
boat = dict()

for _ in range(M):
    a, b = map(int, input().split())
    connect[a].append(b)

for i in range(1, N+1):
    boat[i] = len(connect[i])

def num(a, b):
    return boat[a] * boat[b] - len(set(connect[a]) & set(connect[b]))

answer = 0

for i in range(1, N):
    for j in range(i+1, N+1):
        answer += num(i, j)
print(connect)
print(boat)
print(answer)