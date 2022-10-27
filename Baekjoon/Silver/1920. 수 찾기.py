'''
https://www.acmicpc.net/problem/1920

[문제]

N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.

'''

N = int(input())
num = set(map(int, input().split()))

M = int(input())
candi = list(map(int, input().split()))

for i in candi:
    if i in num:
        print(1)
    else:
        print(0)