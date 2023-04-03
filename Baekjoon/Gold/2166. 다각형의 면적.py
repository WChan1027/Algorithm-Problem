# https://www.acmicpc.net/problem/2166
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())

x, y = [0] * (N+1), [0] * (N+1)

for i in range(N):
    a, b = map(int, input().split())

    x[i], y[i] = a, b

x[-1], y[-1] = x[0], y[0]

part1 = 0
for i in range(N):
    part1 += x[i] * y[i+1]

part2 = 0
for i in range(N):
    part2 += x[i+1] * y[i]

answer = abs(part1 - part2) / 2
print(answer)
