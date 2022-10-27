'''
https://www.acmicpc.net/problem/2751

[문제]

N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

'''
import sys
N = int(sys.stdin.readline())

num = []
for _ in range(N):
    num.append(int(input()))

num.sort()

for i in num:
    print(i)