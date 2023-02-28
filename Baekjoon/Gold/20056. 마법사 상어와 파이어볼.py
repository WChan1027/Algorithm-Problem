# https://www.acmicpc.net/problem/20056
import sys
from pprint import pprint
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M, K = map(int, input().split())

matrix = [[(0, 0, 0, 0)] * N for _ in range(N)]

direction = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
dir1 = [(-1, 0), (0, 1), (1, 0), (0, -1)]
dir2 = [(-1, 1), (1, 1), (1, -1), (-1, -1)]

for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    matrix[r-1][c-1] = (m, s, d, 1)
print('#1')
pprint(matrix)

for move in range(K):
    next_matrix = [[(0, 0, 0, 0)] * N for _ in range(N)]

    for x in range(N):
        for y in range(N):
            if matrix[x][y][3] == 1:
                next_x = (x + direction[matrix[x][y][2]][0] * matrix[x][y][1]) % N
                next_y = (y + direction[matrix[x][y][2]][1] * matrix[x][y][1]) % N

                if next_matrix[next_x][next_y][3] == 0:
                    next_matrix[next_x][next_y] = matrix[next_x][next_y]
                else:
                    next_matrix[next_x][next_y][0] += matrix[next_x][next_y][0]
                    next_matrix[next_x][next_y][1] += matrix[next_x][next_y][1]
                    next_matrix[next_x][next_y][2] %= 2
                    next_matrix[next_x][next_y][2] += matrix[next_x][next_y][2] % 2
                    next_matrix[next_x][next_y][3] += 1

            elif matrix[x][y][3] == 4:
                if matrix[x][y][2] == 10:
                    for dir in dir1:
                        next_x = (x + dir[0] * matrix[x][y][1]) % N
                        next_y = (y + dir[1] * matrix[x][y][1]) % N

                        if next_matrix[next_x][next_y][3] == 0:
                            next_matrix[next_x][next_y] = matrix[next_x][next_y]
                        else:
                            next_matrix[next_x][next_y][0] += matrix[next_x][next_y][0]
                            next_matrix[next_x][next_y][1] += matrix[next_x][next_y][1]
                            next_matrix[next_x][next_y][2] %= 2
                            next_matrix[next_x][next_y][2] += matrix[next_x][next_y][2] % 2
                            next_matrix[next_x][next_y][3] += 1


                elif matrix[x][y][2] == 9:
                    for dir in dir2:
                        next_x = (x + dir[0] * matrix[x][y][1]) % N
                        next_y = (y + dir[1] * matrix[x][y][1]) % N

                        if next_matrix[next_x][next_y][3] == 0:
                            next_matrix[next_x][next_y] = matrix[next_x][next_y]
                        else:
                            next_matrix[next_x][next_y][0] += matrix[next_x][next_y][0]
                            next_matrix[next_x][next_y][1] += matrix[next_x][next_y][1]
                            next_matrix[next_x][next_y][2] %= 2
                            next_matrix[next_x][next_y][2] += matrix[next_x][next_y][2] % 2
                            next_matrix[next_x][next_y][3] += 1


    for x in range(N):
        for y in range(N):
            if next_matrix[x][y][3] > 1:
                next_matrix[x][y][0] //= 5
                next_matrix[x][y][1] //= next_matrix[x][y][3]
                if next_matrix[x][y][2] == 0 or next_matrix[x][y][2] == next_matrix[x][y][3]:
                    next_matrix[x][y][2] = 10
                else:
                    next_matrix[x][y][2] = 9
                next_matrix[x][y][3] = 4
                if next_matrix[x][y][0] == 0:
                    next_matrix[x][y] = (0, 0, 0, 0)

    matrix = next_matrix
    print(f'#{move+2}')
    pprint(matrix)

answer = 0

for x in range(N):
    for y in range(N):
        if matrix[x][y][3] > 0:
            answer += matrix[x][y][0] * matrix[x][y][3]

print(answer)

# matrix = list([{'n': 0} for _ in range(N)] for _ in range(N))        # key, value 형태로 정보 저장
#
# for _ in range(M):
#     r, c, m, s, d = map(int, input().split())
#     r, c = r-1, c-1
#     matrix[r][c]['n'] = 1
#     matrix[r][c]['m'] = m
#     matrix[r][c]['d'] = d
#     matrix[r][c]['s'] = s
#
# direction = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]      # 방향 0~7
# dir1 = [(-1, 0), (0, 1), (1, 0), (0, -1)]       # 방향 0, 2, 4, 6
# dir2 = [(-1, 1), (1, 1), (1, -1), (-1, -1)]     # 방향 1, 3, 5, 7
#
# # K번의 이동
# for move in range(K):
#     next_matrix = list([{'n': 0} for _ in range(N)] for _ in range(N))      # 파이어볼이 이동하는 격자
#
#     # 격자 탐색
#     for x in range(N):
#         for y in range(N):
#             if matrix[x][y]['n'] == 1:      # 1개의 파이어볼이 있을 때
#                 # 그 파이어볼이 이동할 위치
#                 next_x = (x + direction[matrix[x][y]['d']][0] * matrix[x][y]['s']) % N      # matrix[x][y]['d'] : 파이어볼의 방향 , matrix[x][y]['s'] : 파이어볼의 속도
#                 next_y = (y + direction[matrix[x][y]['d']][1] * matrix[x][y]['s']) % N
#
#                 # 파이어볼이 이동한 곳에 아직 파이어볼이 없다면
#                 if next_matrix[next_x][next_y]['n'] == 0:
#                     next_matrix[next_x][next_y]['n'] += 1       # 파이어볼 갯수 + 1
#                     next_matrix[next_x][next_y]['m'] = matrix[x][y]['m']        # 파이어볼 질량
#                     next_matrix[next_x][next_y]['s'] = matrix[x][y]['s']        # 파이어볼 속도
#                     next_matrix[next_x][next_y]['d'] = matrix[x][y]['d']        # 파이어볼 방향
#
#                 # 파이어볼이 이동한 곳에 다른 파이어볼이 있다면
#                 else:
#                     next_matrix[next_x][next_y]['n'] += 1       # 파이어볼 갯수 + 1
#                     next_matrix[next_x][next_y]['m'] += matrix[x][y]['m']       # 파이어볼 질량 더하기
#                     next_matrix[next_x][next_y]['s'] += matrix[x][y]['s']       # 파이어볼 속도 더하기
#                     next_matrix[next_x][next_y]['d'] %= 2       # 기존 파이어볼 방향이 짝수인지 홀수인지 기록
#                     next_matrix[next_x][next_y]['d'] += matrix[x][y]['d'] % 2       # 더해진 파이어볼 방향의 홀짝 값 더하기
#
#             elif matrix[x][y]['n'] == 4:        # 4개로 나뉘어진 파이어볼이 있을 때
#                 if matrix[x][y]['d'] == 10:     # 짝수 방향으로 나뉘어져 있으면
#                     for i in range(4):
#                         next_x = (x + dir1[i][0] * matrix[x][y]['s']) % N
#                         next_y = (y + dir1[i][1] * matrix[x][y]['s']) % N
#
#                         # 파이어볼이 이동한 곳에 아직 파이어볼이 없다면
#                         if next_matrix[next_x][next_y]['n'] == 0:
#                             next_matrix[next_x][next_y]['n'] += 1       # 파이어볼 갯수 + 1
#                             next_matrix[next_x][next_y]['m'] = matrix[x][y]['m']        # 파이어볼 질량
#                             next_matrix[next_x][next_y]['s'] = matrix[x][y]['s']        # 파이어볼 속도
#                             next_matrix[next_x][next_y]['d'] = i*2      # 파이어볼 방향
#
#                         # 파이어볼이 이동한 곳에 다른 파이어볼이 있다면
#                         else:
#                             next_matrix[next_x][next_y]['n'] += 1       # 파이어볼 갯수 + 1
#                             next_matrix[next_x][next_y]['m'] += matrix[x][y]['m']       # 파이어볼 질량 더하기
#                             next_matrix[next_x][next_y]['s'] += matrix[x][y]['s']       # 파이어볼 속도 더하기
#                             next_matrix[next_x][next_y]['d'] %= 2       # 기존 파이어볼 방향이 짝수인지 홀수인지 기록
#                             next_matrix[next_x][next_y]['d'] += matrix[x][y]['d'] % 2       # 더해진 파이어볼 방향의 홀짝 값 더하기
#
#                 elif matrix[x][y]['d'] == 9:        # 홀수 방향으로 나뉘어져 있으면
#                     for i in range(4):
#                         next_x = (x + dir2[i][0] * matrix[x][y]['s']) % N
#                         next_y = (y + dir2[i][1] * matrix[x][y]['s']) % N
#
#                         # 파이어볼이 이동한 곳에 아직 파이어볼이 없다면
#                         if next_matrix[next_x][next_y]['n'] == 0:
#                             next_matrix[next_x][next_y]['n'] += 1       # 파이어볼 파이어볼 갯수 + 1
#                             next_matrix[next_x][next_y]['m'] = matrix[x][y]['m']        # 파이어볼 질량
#                             next_matrix[next_x][next_y]['s'] = matrix[x][y]['s']        # 파이어볼 속도
#                             next_matrix[next_x][next_y]['d'] = i*2 + 1      # 파이어볼 방향
#
#                         # 파이어볼이 이동한 곳에 다른 파이어볼이 있다면
#                         else:
#                             next_matrix[next_x][next_y]['n'] += 1       # 파이어볼 갯수 + 1
#                             next_matrix[next_x][next_y]['m'] += matrix[x][y]['m']       # 파이어볼 질량 더하기
#                             next_matrix[next_x][next_y]['s'] += matrix[x][y]['s']       # 파이어볼 속도 더하기
#                             next_matrix[next_x][next_y]['d'] %= 2       # 기존 파이어볼 방향이 짝수인지 홀수인지 기록
#                             next_matrix[next_x][next_y]['d'] += matrix[x][y]['d'] % 2       # 더해진 파이어볼 방향의 홀짝 값 더하기
#
#     # 이동 완료된 파이어볼 합치기
#     for x in range(N):
#         for y in range(N):
#             # 파이어볼이 있으면
#             if next_matrix[x][y]['n'] > 1:
#
#                 # 파이어볼이 나뉘어졌을 때 질량이 0 이면
#                 if next_matrix[x][y]['m'] < 5:
#                     next_matrix[x][y] = {'n':0}     # 파이어볼 삭제
#
#                 # 파이어볼이 나뉘어지면
#                 else:
#                     next_matrix[x][y]['m'] //= 5    # 파이어볼 질량 나누기
#                     next_matrix[x][y]['s'] //= next_matrix[x][y]['n']       # 파이어볼 속도 나누기
#                     if next_matrix[x][y]['d'] == 0 or next_matrix[x][y]['d'] == next_matrix[x][y]['n']:     # 파이어볼 방향이 모두 홀수 or 짝수 였다면
#                         next_matrix[x][y]['d'] = 10     # 짝수 방향으로 나뉘어짐
#                     else:       # 파이어볼 방향이 홀수, 짝수 섞여 있다면
#                         next_matrix[x][y]['d'] = 9      # 홀수 방향으로 나뉘어짐
#                     next_matrix[x][y]['n'] = 4      # 파이어볼이 나뉘어졌다는 것을 기록
#
#             matrix[x][y] = next_matrix[x][y]        # 이동이 완료된 격자를 현재 격자에 저장
#
# answer = 0
# for x in range(N):
#     for y in range(N):
#         # 파이어볼이 하나 있다면
#         if matrix[x][y]['n'] == 1:
#             answer += matrix[x][y]['m']     # 질량 더하기
#         # 파이어볼이 4개로 나뉘어 있다면
#         elif matrix[x][y]['n'] == 4:
#             answer += matrix[x][y]['m'] * 4     # 질량 4번 더하기
#
# print(answer)