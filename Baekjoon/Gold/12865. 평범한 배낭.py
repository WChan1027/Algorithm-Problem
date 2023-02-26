# https://www.acmicpc.net/problem/12865
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, K = map(int, input().split())

backpack = [0] * (K+1)

stuff = [list(map(int, input().split())) for _ in range(N)]

for item in stuff:
    W, V = item

    for i in range(K, W-1, -1):
        backpack[i] = max(backpack[i], backpack[i-W] + V)

print(backpack[-1])