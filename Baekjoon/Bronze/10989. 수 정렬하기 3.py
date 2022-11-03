'''
https://www.acmicpc.net/problem/10989

[문제]

N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

'''
import sys
N = int(sys.stdin.readline())

num = [0] * 10001

for _ in range(N):
    num[int(sys.stdin.readline())] += 1

for i in range(10001):
    if num[i] != 0:
        for _ in range(num[i]):
            print(i)