# https://www.acmicpc.net/problem/3009
import sys
from collections import defaultdict
sys.stdin = open('input.txt')
input = sys.stdin.readline

dots_x = defaultdict(int)
dots_y = defaultdict(int)

for _ in range(3):
    x, y = map(int, input().split())
    dots_x[x] += 1
    dots_y[y] += 1

for key in dots_x.keys():
    if dots_x[key] % 2:
        answer_x = key

for key in dots_y.keys():
    if dots_y[key] % 2:
        answer_y = key

print(answer_x, answer_y)