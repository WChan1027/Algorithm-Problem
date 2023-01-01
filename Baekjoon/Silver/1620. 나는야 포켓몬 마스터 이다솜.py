# https://www.acmicpc.net/problem/1620
import sys
sys.stdin = open('input.txt')

N, M = map(int, sys.stdin.readline().split())

index = {}
n = 1
number = [str(i) for i in range(1, 10)]
for _ in range(N):
    name = sys.stdin.readline().strip()
    index[str(n)] = name
    n += 1
index_reverse = {key:value for value, key in index.items()}

for _ in range(M):
    quest = sys.stdin.readline().strip()
    if quest in index.keys():
        print(index[quest])
    else:
        print(index_reverse[quest])