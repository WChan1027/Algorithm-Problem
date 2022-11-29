# https://www.acmicpc.net/problem/1764

import sys
sys.stdin = open('input.txt')

N, M = map(int, sys.stdin.readline().split())

no_listen = set()
for _ in range(N):
    no_listen.add(sys.stdin.readline())

no_see = set()
for _ in range(M):
    no_see.add(sys.stdin.readline())

no_listen_see = sorted(list(no_see & no_listen))

print(len(no_listen_see))
for i in no_listen_see:
    print(i)