'''
https://www.acmicpc.net/problem/1929

[문제]

M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.

'''
import sys
M, N = map(int, sys.stdin.readline().split())

def is_prime(M, N):
    for i in range(M, N + 1):
        if i == 2:
            print(2)
        if i == 3:
            print(3)
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                break
            if j == int(i**0.5):
                print(i)

is_prime(M, N)