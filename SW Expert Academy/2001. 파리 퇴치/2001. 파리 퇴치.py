import sys

sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):

    N, M = map(int, input().split())

    matrix = []
    result = 0

    for i in range(N):
        matrix += [list(map(int, input().split()))]

    for i in range(N - M + 1):
        for j in range(N - M + 1):
            catch = 0
            for k in range(i, M + i):
                for l in range(j, M + j):
                    catch += matrix[k][l]
            if catch > result:
                result = catch

    print(f'#{test_case} {result}')