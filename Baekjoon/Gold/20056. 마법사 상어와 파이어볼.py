# https://www.acmicpc.net/problem/20056
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M, K = map(int, input().split())

matrix = list([{'n':0} for _ in range(N)] for _ in range(N))

for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    r, c = r-1, c-1
    matrix[r][c]['n'] = 1
    matrix[r][c]['m'] = m
    matrix[r][c]['d'] = d
    matrix[r][c]['s'] = s

direction = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
dir1 = [(-1, 0), (0, 1), (1, 0), (0, -1)]
dir2 = [(-1, 1), (1, 1), (1, -1), (-1, -1)]

for move in range(K):
    next_matrix = list([{'n': 0} for _ in range(N)] for _ in range(N))

    for x in range(N):
        for y in range(N):
            if matrix[x][y]['n'] == 1:
                next_x = (x + direction[matrix[x][y]['d']][0] * matrix[x][y]['s']) % N
                next_y = (y + direction[matrix[x][y]['d']][1] * matrix[x][y]['s']) % N

                if next_matrix[next_x][next_y]['n'] == 0:
                    next_matrix[next_x][next_y]['n'] = 1
                    next_matrix[next_x][next_y]['m'] = matrix[x][y]['m']
                    next_matrix[next_x][next_y]['s'] = matrix[x][y]['s']
                    next_matrix[next_x][next_y]['d'] = matrix[x][y]['d']

                else:
                    next_matrix[next_x][next_y]['n'] += 1
                    next_matrix[next_x][next_y]['m'] += matrix[x][y]['m']
                    next_matrix[next_x][next_y]['s'] += matrix[x][y]['s']
                    if next_matrix[next_x][next_y]['n'] == 2:
                        next_matrix[next_x][next_y]['d'] %= 2
                    next_matrix[next_x][next_y]['d'] += matrix[x][y]['d'] % 2

            elif matrix[x][y]['n'] == 4:
                if matrix[x][y]['d'] == -2:
                    for i in range(4):
                        next_x = (x + dir1[i][0] * matrix[x][y]['s']) % N
                        next_y = (y + dir1[i][1] * matrix[x][y]['s']) % N
                        if next_matrix[next_x][next_y]['n'] == 0:
                            next_matrix[next_x][next_y]['n'] = 1
                            next_matrix[next_x][next_y]['m'] = matrix[x][y]['m']
                            next_matrix[next_x][next_y]['s'] = matrix[x][y]['s']
                            next_matrix[next_x][next_y]['d'] = i*2

                        else:
                            next_matrix[next_x][next_y]['n'] += 1
                            next_matrix[next_x][next_y]['m'] += matrix[x][y]['m']
                            next_matrix[next_x][next_y]['s'] += matrix[x][y]['s']
                            if next_matrix[next_x][next_y]['n'] == 2:
                                next_matrix[next_x][next_y]['d'] %= 2
                            next_matrix[next_x][next_y]['d'] += matrix[x][y]['d'] % 2

                elif matrix[x][y]['d'] == -1:
                    for i in range(4):
                        next_x = (x + dir2[i][0] * matrix[x][y]['s']) % N
                        next_y = (y + dir2[i][1] * matrix[x][y]['s']) % N
                        if next_matrix[next_x][next_y]['n'] == 0:
                            next_matrix[next_x][next_y]['n'] += 1
                            next_matrix[next_x][next_y]['m'] = matrix[x][y]['m']
                            next_matrix[next_x][next_y]['s'] = matrix[x][y]['s']
                            next_matrix[next_x][next_y]['d'] = i*2 + 1

                        else:
                            next_matrix[next_x][next_y]['n'] += 1
                            next_matrix[next_x][next_y]['m'] += matrix[x][y]['m']
                            next_matrix[next_x][next_y]['s'] += matrix[x][y]['s']
                            if next_matrix[next_x][next_y]['n'] == 2:
                                next_matrix[next_x][next_y]['d'] %= 2
                            next_matrix[next_x][next_y]['d'] += matrix[x][y]['d'] % 2

    for x in range(N):
        for y in range(N):
            if next_matrix[x][y]['n'] > 1:
                if next_matrix[x][y]['m'] < 5:
                    next_matrix[x][y] = {'n':0}
                else:
                    next_matrix[x][y]['m'] //= 5
                    next_matrix[x][y]['s'] //= next_matrix[x][y]['n']
                    if next_matrix[x][y]['d'] == 0 or next_matrix[x][y]['d'] == next_matrix[x][y]['n']:
                        next_matrix[x][y]['d'] = -2
                    else:
                        next_matrix[x][y]['d'] = -1
                    next_matrix[x][y]['n'] = 4

    matrix = next_matrix[:]

answer = 0
for x in range(N):
    for y in range(N):
        if matrix[x][y]['n'] == 1:
            answer += matrix[x][y]['m']
        elif matrix[x][y]['n'] == 4:
            answer += matrix[x][y]['m'] * 4

print(answer)