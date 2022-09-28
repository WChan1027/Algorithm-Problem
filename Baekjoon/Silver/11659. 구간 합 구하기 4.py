'''
https://www.acmicpc.net/problem/11659

[문제]

수 N개가 주어졌을 때, i번째 수부터 j번째 수까지 합을 구하는 프로그램을 작성하시오.

'''


N, M = map(int, input().split())

num = list(map(int, input().split()))

temp_sum = [0]
temp = 0

for i in num:
    temp = temp + i
    temp_sum.append(temp)

for _ in range(M):
    i, j = map(int, input().split())
    print(temp_sum[j] - temp_sum[i-1])