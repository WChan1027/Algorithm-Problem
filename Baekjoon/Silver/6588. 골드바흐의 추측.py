# https://www.acmicpc.net/problem/6588

import sys

sys.stdin = open('input.txt')

number = [1] * 1000001
number[0], number[1] = 0, 0
n = 1
while n < 500000:
    n += 1
    if number[n] == 1:
        for i in range(n, 1000001, n):
            number[i] = 0
        number[n] = 1

while True:
    num = int(sys.stdin.readline())
    if num == 0:
        break

    for i in range(2, 1000001):
        if number[i] == 1:
            if number[num - i] == 1:
                print(f'{num} = {i} + {num - i}')
                break