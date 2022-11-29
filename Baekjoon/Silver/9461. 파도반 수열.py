# https://www.acmicpc.net/problem/9461
import sys
sys.stdin = open('input.txt')

T = int(sys.stdin.readline())

num = [0] * 101
num[1] = 1
num[2] = 1

for i in range(3, 101):
    num[i] = num[i-2] + num[i-3]

for test_case in range(T):
    N = int(sys.stdin.readline())

    print(num[N])