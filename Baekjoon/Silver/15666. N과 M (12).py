# https://www.acmicpc.net/problem/15666
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
num = sorted(list(map(int, input().split())))
result = []

def calc(n, m, array):
    if n == M:
        result.append(tuple(array))
        return

    for i in range(m, N):
        calc(n + 1, i, array + [num[i]])

calc(0, 0, [])

result = list(dict.fromkeys(tuple(result)))
for answer in result:
    print(*answer)