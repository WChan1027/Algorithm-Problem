# https://www.acmicpc.net/problem/20291
import sys
from collections import defaultdict
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())

file = defaultdict(int)

for _ in range(N):
    file[input().strip().split('.')[1]] += 1

result = sorted(file.keys())

for answer in result:
    print(answer, file[answer])