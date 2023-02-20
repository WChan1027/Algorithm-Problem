# https://www.acmicpc.net/problem/1149
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())

value = [list(map(int, input().split())) for _ in range(N)]

min_value = [[0, 0, 0] for _ in range(N)]

min_value[0] = value[0]

for i in range(1, N):
    min_value[i] = [min(min_value[i-1][1], min_value[i-1][2]) + value[i][0],
                 min(min_value[i-1][0], min_value[i-1][2]) + value[i][1],
                 min(min_value[i-1][0], min_value[i-1][1]) + value[i][2]]

answer = min(min_value[N-1])

print(answer)