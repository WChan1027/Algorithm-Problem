# https://www.acmicpc.net/problem/1510
import sys
from itertools import combinations
sys.stdin = open('input.txt')
input = sys.stdin.readline
N, M = map(int, input().split())

answer = 0

dots = list(i for i in range(N*M))

for triangle in combinations(dots, 3):
    a, b, c = triangle
    a_x, a_y = a // M, a % M
    b_x, b_y = b // M, b % M
    c_x, c_y = c // M, c % M

    if a_x == b_x == c_x or a_y == b_y == c_y:
        pass

    else:
        if (a_x - b_x) * (a_x - c_x) * (b_x - c_x) == 0:
            length1 = ((a_x - b_x) * (a_x - b_x) + (a_y - b_y) * (a_y - b_y)) ** (1/2)
            length2 = ((b_x - c_x) * (b_x - c_x) + (b_y - c_y) * (b_y - c_y)) ** (1/2)
            length3 = ((a_x - c_x) * (a_x - c_x) + (a_y - c_y) * (a_y - c_y)) ** (1/2)

            if len(set([length1, length2, length3])) < 3:
                answer += 1

        else:
            gradient1 = (c_y - a_y) / (c_x - a_x)
            gradient2 = (b_y - a_y) / (b_x - a_x)

            if gradient1 == gradient2:
                pass

            else:
                length1 = ((a_x - b_x) * (a_x - b_x) + (a_y - b_y) * (a_y - b_y)) ** (1/2)
                length2 = ((b_x - c_x) * (b_x - c_x) + (b_y - c_y) * (b_y - c_y)) ** (1/2)
                length3 = ((a_x - c_x) * (a_x - c_x) + (a_y - c_y) * (a_y - c_y)) ** (1/2)

                if len(set([length1, length2, length3])) < 3:
                    answer += 1

print(answer)
#
# n = [[0] * (M+1) for _ in range(N+1)]
# n[2][2] = 4
#
# for i in range(3, N+1):
#     n[i][2] = n[i-1][2] * 2 - n[i-2][2]
#
#     if i % 2 == 1:
#         n[i][2] += 2
#
# for i in range(3, M+1):
#     n[2][i] = n[2][i-1] * 2 - n[2][i-2]
#
#     if i % 2 == 1:
#         n[2][i] += 2
#
# for i in range(3, N+1):
#     for j in range(3, M+1):
#         n[i][j] += n[i-1][j-1]
#         n[i][j] += (n[i-1][j] - n[i-2][j]) * 2
#         n[i][j] += (n[i][j-1] - n[i][j-2]) * 2
#
#
#         if i % 2 == 1:
#             n[i][j] += 2
#
#         if j % 2 == 1:
#             n[i][j] += 2
#
#         if i == j:
#             n[i][j] += (j-2) * 4
#             n[i][j] += 4
#         else:
#             if i > 2 and j > 2:
#                 if 2*j > i or 2*i > j:
#                     n[i][j] += 4
#
# for a in n:
#     print(*a)



# num = [[0] * (M+1) for _ in range(N+1)]
# num[2][2] = 4
#
# for i in range(3, M):
#     for j in range(2, i+1):
#         num[2][i] += n[2][j] * (i+1-j)
#
# for a in num:
#     print(*a)