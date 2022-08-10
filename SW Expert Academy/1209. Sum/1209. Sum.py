import sys

sys.stdin = open('input.txt')

T = 10

for test_case in range(T):
    tc = sys.stdin.readline()
    matrix = []
    for i in range(100):
        matrix.append(list(map(int, sys.stdin.readline().split())))
    sum_max = 0
    for i in range(100):
        sum_line = 0
        sum_row = 0

        for j in range(100):
            sum_line += matrix[i][j]
            sum_row += matrix[j][i]
        if sum_line > sum_max:
            sum_max = sum_line
        if sum_row > sum_max:
            sum_max = sum_row

    for i in range(2):
        sum_diagonal = 0
        for j in range(100):
            sum_diagonal += matrix[j+(-2*j*i)][j+(-2*j*i)]
        if sum_diagonal > sum_max:
            sum_max = sum_diagonal

    print(f'#{tc} {sum_max}')