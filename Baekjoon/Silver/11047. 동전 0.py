# https://www.acmicpc.net/problem/11047

import sys

sys.stdin = open('input.txt')

N, K = map(int, sys.stdin.readline().split())

price = []
for _ in range(N):
    price.append(int(sys.stdin.readline()))

count = 0
idx = len(price) - 1
while K > 0:
    if price[idx] <= K:
        K -= price[idx]
        count += 1
    else:
        idx -= 1

print(count)