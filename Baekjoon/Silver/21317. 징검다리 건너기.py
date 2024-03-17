# https://www.acmicpc.net/problem/21317
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
dp = [[0, 0] for _ in range(N)]

for i in range(1, N):
    dp[i] = list(map(int, input().split()))

K = int(input())

for i in range(2, N):

print(dp)