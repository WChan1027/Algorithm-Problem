# https://www.acmicpc.net/problem/10830
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, B = map(int, input().split())

procession = [list(map(int, input().split())) for _ in range(N)]

def matrix_multiple(A, B):
    length = len(A)
    matrix = [[0] * length for _ in range(length)]
    for i in range(length):
        for j in range(length):
            for k in range(length):
                matrix[i][j] += A[i][k] * B[k][j]
            matrix[i][j] %= 1000
    return matrix


def devide_conquer(matrix, n):
    if n == 1:
        return matrix

    if n % 2 == 0:
        result = devide_conquer(matrix, n//2)
        return matrix_multiple(result, result)

    else:
        result = devide_conquer(matrix, n//2)
        a = matrix_multiple(result, result)
        return matrix_multiple(matrix, a)

if B == 1:
    for i in range(N):
        for j in range(N):
            procession[i][j] %= 1000

    for row in procession:
        print(*row)

else:
    answer = devide_conquer(procession, B)
    for row in answer:
        print(*row)