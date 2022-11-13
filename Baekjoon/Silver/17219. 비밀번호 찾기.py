# https://www.acmicpc.net/problem/17219

import sys
sys.stdin = open('input.txt')

N, M = map(int, sys.stdin.readline().split())

memo = {}
for _ in range(N):
    site, PW = map(str, sys.stdin.readline().split())
    memo[site] = PW

for _ in range(M):
    want = input()
    print(memo[want])