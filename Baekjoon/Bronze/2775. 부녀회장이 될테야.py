# https://www.acmicpc.net/problem/2775
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

T = int(input())

for test_case in range(T):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())

    # 아파트
    resident = [[0]*n for _ in range(k+1)]
    # 1층 각호의 주민 수
    for i in range(n):
        resident[0][i] = i+1

    # k층까지 n호까지의 주민 수
    for i in range(1, k+1):
        for j in range(n):
            resident[i][j] = sum(resident[i-1][0:j+1])

    print(resident[k][n-1])