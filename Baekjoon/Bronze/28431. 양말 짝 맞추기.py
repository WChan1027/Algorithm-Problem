import sys
from collections import defaultdict
sys.stdin = open('input.txt')
input = sys.stdin.readline

socks = defaultdict(int)

for _ in range(5):
    socks[int(input())] += 1

for i in socks:
    if socks[i]%2:
        answer = i
        break

print(answer)