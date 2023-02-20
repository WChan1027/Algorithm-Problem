# https://www.acmicpc.net/problem/9465
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

T = int(input())

for test_case in range(T):
    n = int(input())
    score = [list(map(int, input().split())) for _ in range(2)]

    result = [[0] * n for _ in range(2)]
    if n == 1:
        print(max(score[0][0], score[1][0]))

    else:
        result[0][0] = score[0][0]
        result[1][0] = score[1][0]

        result[0][1] = score[1][0] + score[0][1]
        result[1][1] = score[0][0] + score[1][1]

        if n == 2:
            print(max(result[0][1], result[1][1]))

        else:
            for i in range(2, n):
                result[0][i] = max(result[1][i-1], result[1][i-2]) + score[0][i]
                result[1][i] = max(result[0][i-1], result[0][i-2]) + score[1][i]

            print(max(result[0][n-1], result[1][n-1]))