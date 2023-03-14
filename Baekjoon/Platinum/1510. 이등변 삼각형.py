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