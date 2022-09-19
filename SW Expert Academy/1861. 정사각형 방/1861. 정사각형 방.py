import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    matrix = []
    for _ in range(N):
        matrix.append(list(map(int, input().split())))

    result = [N*N, 0]

    for i in range(N):
        count = 1
        for j in range(N):
            count = 1
            a, b = i, j
            while True:
                flag = 0
                if j < N-1 and matrix[i][j] + 1 == matrix[i][j+1]:
                    count += 1
                    flag = 1
                    j = j+1
                elif i < N-1 and matrix[i][j] + 1 == matrix[i+1][j]:
                    count += 1
                    flag = 1
                    i = i+1
                elif j > 0 and matrix[i][j] + 1 == matrix[i][j-1]:
                    count += 1
                    flag = 1
                    j = j-1
                elif i > 0 and matrix[i][j] + 1 == matrix[i-1][j]:
                    count += 1
                    flag = 1
                    i = i-1

                if flag == 0:
                    break
            if count > result[1]:
                result = [matrix[a][b], count]
            elif count == result[1]:
                if matrix[a][b] < result[0]:
                    result = [matrix[a][b], count]

    print(f'#{test_case} {result[0]} {result[1]}')
