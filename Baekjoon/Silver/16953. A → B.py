# https://www.acmicpc.net/problem/16953
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

A, B = map(int, input().split())

answer = 1
while B > A:
    if B % 2 == 0:
        B //= 2
        answer += 1

    else:
        if B % 10 == 1:
            B //= 10
            answer += 1

        else:
            break

if B == A:
    print(answer)
else:
    print(-1)