# https://www.acmicpc.net/problem/9020
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

T = int(input())

number = [1] * 1000001
number[0], number[1] = 0, 0
n = 1
while n < 5000:
    n += 1
    if number[n] == 1:
        for i in range(n, 10001, n):
            number[i] = 0
        number[n] = 1

for _ in range(T):
    num = int(input())

    for i in range(num//2, 10001):
        if number[i] == 1:
            if number[num - i] == 1:
                print(num - i, i)
                break