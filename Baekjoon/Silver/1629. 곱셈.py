# https://www.acmicpc.net/problem/1629
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

A, B, C = map(int, input().split())

remain = [1, A % C]
n = 1
B -= 1
while B > 0:
    N = 2 ** (n-1)
    if B >= N:
        remain.append((remain[-1] * remain[n]) % C)
        B -= N
        n += 1
    else:
        n -= 1

print(remain[-1])