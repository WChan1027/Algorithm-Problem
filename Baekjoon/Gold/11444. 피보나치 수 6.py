# https://www.acmicpc.net/problem/11444
import sys
from time import time
start = time()
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())

def matrix_multiple(A, B):
    matrix = [[0, 0], [0, 0]]
    matrix[0][0] = (A[0][0] * B[0][0] + A[0][1] * B[1][0]) % 1000000007
    matrix[0][1] = (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % 1000000007
    matrix[1][0] = (A[1][0] * B[0][0] + A[1][1] * B[1][0]) % 1000000007
    matrix[1][1] = (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % 1000000007
    return matrix

fibonacci = [[1, 1], [1, 0]]

def devide_conquer(fibo, n):
    if n == 1:
        return fibo

    if n % 2 == 0:
        result = devide_conquer(fibo, n//2)
        return matrix_multiple(result, result)

    else:
        result = devide_conquer(fibo, n // 2)
        a = matrix_multiple(result, result)
        return matrix_multiple(a, fibo)

answer = devide_conquer(fibonacci, n)
print(answer[0][1])

end = time()
print(end - start)