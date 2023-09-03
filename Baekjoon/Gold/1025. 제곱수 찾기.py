# https://www.acmicpc.net/problem/1025

N, M = map(int, input().split())

nums = [list(map(int, input())) for _ in range(N)]

def square_num(n, m):
    num = f'{nums[n][m]}'
    if int(num)**(1/2) % 1 == 0:
        candi.append(int(num))
    for i in range(-n, N-n):
        for j in range(-m, M-m):
            num = f'{nums[n][m]}'
            a, b = n, m
            if i == 0 and j == 0:
                pass
            else:
                while True:
                    next_i, next_j = a+i, b+j
                    if 0 <= next_i < N and 0 <= next_j < M:
                        a, b = next_i, next_j
                        num += f'{nums[a][b]}'
                        if int(num) ** (1 / 2) % 1 == 0:
                            candi.append(int(num))
                    else:
                        break

candi = []

for i in range(N):
    for j in range(M):
        square_num(i, j)

if not candi:
    print(-1)
else:
    print(max(candi))