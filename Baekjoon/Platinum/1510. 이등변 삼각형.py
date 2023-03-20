# https://www.acmicpc.net/problem/1510
import sys
from itertools import combinations
import math
sys.stdin = open('input.txt')
input = sys.stdin.readline


N, M = map(int, input().split())

answer = 0

dots = list(i for i in range(N*M))

tri = 0
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
                if max(a_x, b_x, c_x) == N-1 and max(a_y, b_y, c_y) == M-1 and min(a_x, b_x, c_x) == 0 and min(a_y, b_y, c_y) == 0:
                    print((a_x, a_y), (b_x, b_y), (c_x, c_y))
                    tri += 1

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
                    if max(a_x, b_x, c_x) == N-1 and max(a_y, b_y, c_y) == M-1 and min(a_x, b_x, c_x) == 0 and min(a_y, b_y, c_y) == 0:
                        print((a_x, a_y), (b_x, b_y), (c_x, c_y))
                        tri += 1

print(tri)
print(answer)

new = [[0] * (M+1) for _ in range(N+1)]

for i in range(2, N+1):
    for j in range(2, M+1):
        if i == j:
            new[i][j] += (i-1) * 4
            new[i][j] += (i//2-1) * 4

            for x in range(1, i):
                l = (2*(i-1)*x) ** (1/2)
                if l != (i-x) and l < (i-1) and not l % 1:
                    print(i, x, l)
                    new[i][j] += 8


        else:



            # if abs(i - j) < min(i-1, j-1):
            #     new[i][j] += 4
            #
            # a, b = min(i-1, j-1), max(i-1, j-1)
            # theta = math.atan(a/b)
            # x = a / math.sin(2 * theta)
            # if not x % 1:
            #     new[i][j] += 4
            #
            # c = (b ** 2 - a ** 2) ** (1/2)
            # if not c % 1:
            #     new[i][j] += 4
            #
            # for x in range(1, a+1):
            #     d = ((b ** 2 + x ** 2) - (a ** 2)) ** (1/2)
            #     e = ((b ** 2 + x ** 2) - ((a - x) ** 2)) ** (1 / 2)
            #     f = ((a ** 2 + x ** 2) - ((b - x) ** 2))
            #     h = ((a ** 2 + b ** 2) - x ** 2) / (2*b)
            #     if not d % 1 and d < b:
            #         new[i][j] += 4
            #
            #     elif not e % 1 and e < b:
            #         new[i][j] += 4
            #
            #     elif f > 0:
            #         f = f ** (1 / 2)
            #         if not f % 1 and int(f) != x and f < a:
            #             new[i][j] += 4
            #
            #     elif x < a and int(h) != b and int(h) != a and not h % 1 and h < b:
            #         # print(a, b, x, h)
            #         new[i][j] += 4

            middle = b/2
            for x in range(int(middle)):
                g = a/2 + (middle - x) * (b / a)
                if not g % 1 and g < a:
                    new[i][j] += 4


        if i % 2:
            new[i][j] += 2
        if j % 2:
            new[i][j] += 2



for a in new:
    print(*a)

answer = 0
for i in range(1, N + 1):
    for j in range(1, M + 1):
        answer += new[i][j] * (N + 1 - i) * (M + 1 - j)

print(answer)