# https://www.acmicpc.net/problem/1107

import sys

N = sys.stdin.readline()
M = int(sys.stdin.readline())

broken = list(map(str, sys.stdin.readline().split()))

count = abs(int(N) - 100)

for i in range(1000001):
    for j in range(len(str(i))):
        if str(i)[j] in broken:
            break
        elif j == len(str(i))-1:
            count = min(count, len(str(i)) + abs(int(N) - i))

print(count)
