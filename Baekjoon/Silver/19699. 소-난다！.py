# https://www.acmicpc.net/problem/19699
import sys
from itertools import combinations
sys.stdin = open('input.txt')
input = sys.stdin.readline

def check_prime(num):
    for i in range(2, num//2 + 1):
        if num % i == 0:
            return 0
    else:
        return 1

N, M = map(int, input().split())
H = list(map(int, input().split()))

combi = set(sum(i) for i in (combinations(H, M)))
answer = []

for num in combi:
    if check_prime(num) == 1:
        answer.append(num)

answer.sort()
if answer:
    print(*answer)
else:
    print(-1)