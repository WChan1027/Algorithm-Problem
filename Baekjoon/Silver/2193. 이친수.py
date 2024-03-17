# https://www.acmicpc.net/problem/2193
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def pinary_number(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1

    dp = [[0, 0] for _ in range(n + 1)]

    dp[1][0] = 0
    dp[1][1] = 1
    dp[2][0] = 1
    dp[2][1] = 0

    for i in range(3, n + 1):
        dp[i][0] = dp[i - 1][0] + dp[i - 1][1]
        dp[i][1] = dp[i - 1][0]

    total = dp[n][0] + dp[n][1]
    return total

n = int(input())

answer = pinary_number(n)
print(answer)