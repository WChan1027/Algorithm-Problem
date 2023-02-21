# https://www.acmicpc.net/problem/11660
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(N)]
sum_matrix = [[0] * (N+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, N+1):
        sum_matrix[i][j] = sum_matrix[i-1][j] + sum_matrix[i][j-1] - sum_matrix[i-1][j-1] + matrix[i-1][j-1]

for test_case in range(M):
    x1, y1, x2, y2 = map(int, input().split())

    print(sum_matrix[x2][y2] - sum_matrix[x2][y1-1] - sum_matrix[x1-1][y2] + sum_matrix[x1-1][y1-1])