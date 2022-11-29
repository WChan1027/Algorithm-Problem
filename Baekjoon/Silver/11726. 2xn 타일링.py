# https://www.acmicpc.net/problem/11726

import sys
sys.stdin = open('input.txt')

n = int(sys.stdin.readline())
count = [0] * (n+1)
count[1] = 1
if n > 1:
    count[2] = 2

if n > 2:
    for i in range(3, n+1):
        count[i] = count[i-1] + count[i-2]

print(count[n] % 10007)