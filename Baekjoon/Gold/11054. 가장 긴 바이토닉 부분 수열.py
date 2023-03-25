# https://www.acmicpc.net/problem/11054
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())

sequence = list(map(int, input().split()))
sequence_reverse = sequence[::-1]
dp = [1] * N
dp_reverse = [1] * N

for i in range(N):
    for j in range(i):
        if sequence[i] > sequence[j]:
            dp[i] = max(dp[i], dp[j] + 1)

        if sequence_reverse[i] > sequence_reverse[j]:
            dp_reverse[i] = max(dp_reverse[i], dp_reverse[j] + 1)

answer = 0
for i in range(N):
    answer = max(answer, dp[i] + dp_reverse[N-i-1]-1)

print(answer)