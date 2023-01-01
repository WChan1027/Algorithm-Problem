# https://www.acmicpc.net/problem/1547
import sys
sys.stdin = open('input.txt')

M = int(sys.stdin.readline())

cup = 1
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    if a == cup:
        cup = b
    elif b == cup:
        cup = a

print(cup)