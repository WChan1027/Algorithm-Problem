'''
https://www.acmicpc.net/problem/11050

[문제]

자연수 N과 정수 K가 주어졌을 때 이항 계수를 구하는 프로그램을 작성하시오.

'''

N, K = map(int, input().split())

up, down = 1, 1

for i in range(N, N-K, -1):
    up *= i

for i in range(1, K+1):
    down *= i

answer = up // down
print(answer)