# https://www.acmicpc.net/problem/25304
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

X = int(input())
N = int(input())

stuffs = [list(map(int, input().split())) for _ in range(N)]

result = 0
for price in stuffs:
    result += price[0] * price[1]

if X == result:
    print('Yes')
else:
    print('No')