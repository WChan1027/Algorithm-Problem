'''
https://www.acmicpc.net/problem/2738

[문제]

N*M크기의 두 행렬 A와 B가 주어졌을 때, 두 행렬을 더하는 프로그램을 작성하시오.

'''

N, M = map(int, input().split())
A, B = [], []
answer = ''
for i in range(N):
    A += [list(map(int, input().split()))]

for i in range(N):
    B += [list(map(int, input().split()))]

for i in range(N):
    for j in range(M):
        answer += f'{A[i][j] + B[i][j]} '
    print(answer)
    answer = ''
