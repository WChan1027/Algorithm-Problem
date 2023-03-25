# https://www.acmicpc.net/problem/1510
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())

new = [[0] * (M+1) for _ in range(N+1)]

for i in range(2, N+1):
    for j in range(2, M+1):
        # a : 짧은 변 길이, b : 긴 변 길이
        a, b = min(i-1, j-1), max(i-1, j-1)

        # a가 짝수일 때
        if not a % 2:
            new[i][j] += 2

        # b가 짝수일 때
        if not b % 2:
            new[i][j] += 2

        # 정사각형일 때
        if a == b:

            # 꼭지점 세 개를 포함하는 이등변 삼각형
            new[i][j] += 4

            # 꼭지점 두 개를 포함하는 이등변 삼각형
            new[i][j] += (i//2 - 1) * 4

            # 꼭지점 한 개를 포함하는 이등변 삼각형
            # 5 x 5 의 경우 (0, 0), (5, 3), (3, 5)
            new[i][j] += (i-2) * 4

            # 8 x 8 의 경우 (0, 0), (1, 8), (8, 4)
            for x in range(1, a):
                l = (2*a*x) ** (1/2)
                if l != (a-x) and l < a and not l % 1:
                    new[i][j] += 8

        else:
            # 꼭지점 두 개를 포함하는 이등변 삼각형
            for x in range(1, a//2):
                c = b/2 + (a/2 - x) * (a / b)
                if not c % 1 and c < b:
                    new[i][j] += 4

            for x in range(1, b):
                if b ** 2 == a ** 2 + x ** 2:
                    new[i][j] += 4
                if x == ((b-x) ** 2 + a ** 2) ** (1/2):
                    new[i][j] += 2
                if b == (a ** 2 + x ** 2) ** (1/2) + x:
                    new[i][j] += 2

                # 꼭지점 한 개를 포함하는 이등변 삼각형
                d1 = a ** 2 + x ** 2 - (b-x) ** 2
                d2 = a ** 2 + (b-x) ** 2 - x ** 2
                if d1 > 0:
                    d1 = d1 ** (1/2)
                    if not d1 % 1 and 0 < d1 < a:
                        new[i][j] += 2
                if d2 > 0:
                    d2 = d2 ** (1/2)
                    if not d2 % 1 and 0 < d2 < a:
                        new[i][j] += 2

                e1 = a ** 2 + x ** 2 - b ** 2
                e2 = (b-x) ** 2 + a ** 2 - b ** 2
                if e1 > 0:
                    e1 = e1 ** (1/2)
                    if not e1 % 1 and 0 < e1 < a:
                        new[i][j] += 2
                if e2 > 0:
                    e2 = e2 ** (1/2)
                    if not e2 % 1 and 0 < e2 < a:
                        new[i][j] += 2

                f1 = (b ** 2 - (b-x) ** 2 + a ** 2) / (2 * a)
                f2 = (a ** 2 + b ** 2 - x ** 2) / (2 * a)
                if not f1 % 1 and 0 < f1 < a:
                    new[i][j] += 2
                if not f2 % 1 and 0 < f2 < a:
                    new[i][j] += 2

answer = 0
for i in range(2, N + 1):
    for j in range(2, M + 1):
        answer += new[i][j] * (N + 1 - i) * (M + 1 - j)

print(answer)