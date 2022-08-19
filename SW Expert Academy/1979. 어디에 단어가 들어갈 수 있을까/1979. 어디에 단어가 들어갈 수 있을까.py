import sys

sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    N, K = map(int, input().split())

    matrix = []
    space = 1
    result = 0

    for _ in range(N):
        matrix += [list(map(int, input().split()))]

    for i in range(N):
        for j in range(N - K + 1):
            for k in range(K):
                space *= matrix[i][j+k]
            if space == 1:
                if j == (N - K):
                    if matrix[i][j-1] == 0:
                        result += 1
                elif j == 0:
                    if matrix[i][j+K] == 0:
                        result += 1
                else:
                    if matrix[i][j+K] == 0 and matrix[i][j-1] == 0:
                        result += 1
            space = 1

            for k in range(K):
                space *= matrix[j+k][i]
            if space == 1:
                if j == (N - K):
                    if matrix[j-1][i] == 0:
                        result += 1
                elif j == 0:
                    if matrix[j+K][i] == 0:
                        result += 1
                else:
                    if matrix[j+K][i] == 0 and matrix[j-1][i] == 0:
                        result += 1
            space = 1

    print(f'#{test_case} {result}')