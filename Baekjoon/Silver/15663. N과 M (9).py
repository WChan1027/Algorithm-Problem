# https://www.acmicpc.net/problem/15663
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
num = sorted(list(map(int, input().split())))
visited = [0] * N
result = []

def calc(n, array):
    if n == M:
        result.append(tuple(array))
        return

    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            calc(n + 1, array + [num[i]])
            visited[i] = 0

calc(0, [])

result = list(dict.fromkeys(tuple(result)))
for answer in result:
    print(*answer)