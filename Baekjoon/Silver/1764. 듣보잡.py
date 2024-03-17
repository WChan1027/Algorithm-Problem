import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())

no_listen = set()
for _ in range(N):
    no_listen.add(input().strip())

no_see = set()
for _ in range(M):
    no_see.add(input().strip())

no_listen_see = list(no_see & no_listen)

print(len(no_listen_see))
for i in no_listen_see:
    print(i)