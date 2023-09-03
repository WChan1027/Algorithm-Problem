import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

b1, b2, b3 = map(int, input().split())

dp = [[0] * 501 for _ in range(501)]
dp[b1][0], dp[b2][0], dp[b3][0], dp[0][b1], dp[0][b2], dp[0][b3] = 1, 1, 1, 1, 1, 1

for _ in range(5):
    k1, k2 = map(int, input().split())

    