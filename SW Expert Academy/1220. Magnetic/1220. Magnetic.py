import sys

sys.stdin = open('input.txt')

for test_case in range(1, 11):
    N = int(input())
    table = []
    for _ in range(100):
        table += [list(map(int, input().split()))]

    result = 0

    for i in range(N):
        index_y = 0
        while index_y < 99:
            if table[index_y][i] == 1:
                for k in range(index_y+1, N):
                    if table[k][i] == 2:
                        result += 1
                        index_y = k
                        break
                    elif k == N-1:
                        index_y = k
            else:
                index_y += 1

    print(f'#{test_case} {result}')