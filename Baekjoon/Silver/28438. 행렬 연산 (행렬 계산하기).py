import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M, Q = map(int, input().split())

matrix_row = [0] * N
matrix_column = [0] * M

for _ in range(Q):
    a, b, c = map(int, input().split())
    if a == 1:
        matrix_row[b-1] += c

    else:
        matrix_column[b-1] += c

for i in range(N):
    result = [matrix_row[i]] * M
    for j in range(M):
        result[j] += matrix_column[j]

    print(*result)