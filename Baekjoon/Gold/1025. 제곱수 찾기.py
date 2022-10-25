'''
https://www.acmicpc.net/problem/1025

[문제]

N행 M열의 표 A가 있고, 표의 각 칸에는 숫자가 하나씩 적혀있다.
연두는 서로 다른 1개 이상의 칸을 선택하려고 하는데, 행의 번호가 선택한 순서대로 등차수열을 이루고 있어야 하고,
열의 번호도 선택한 순서대로 등차수열을 이루고 있어야 한다. 이렇게 선택한 칸에 적힌 수를 순서대로 이어붙이면 정수를 하나 만들 수 있다.
연두가 만들 수 있는 정수 중에서 가장 큰 완전 제곱수를 구해보자.
완전 제곱수란 어떤 정수를 제곱한 수이다.

'''

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