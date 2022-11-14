# https://www.acmicpc.net/problem/6588

import sys

sys.stdin = open('input.txt')

number = [0] * 1000001
n = 1
while n < 500000:
    n += 1
    if number[n] == 0:
        for i in range(n, 1000001, n):
            number[i] = 1
        number[n] = 0

while True:
    num = int(sys.stdin.readline())
    if num == 0:
        break

    for i in range(len(number)):
        if number[i] == 1:
            if number[num - number[i]] == 1:
                print(f'{num} = {number[i]} + {num - number[i]}')
                break