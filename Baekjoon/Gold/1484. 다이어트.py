# https://www.acmicpc.net/problem/1484
import sys
sys.stdin = open('input.txt')

G = int(sys.stdin.readline())

result = []
a = 2
while True:
    if a**2 - (a-1)**2 > G:
        break

    b = 1
    while b < a:
        if a**2 - b**2 == G:
            result.append(a)
            break

        b += 1

    a += 1

if result:
    for i in result:
        print(i)
else:
    print(-1)