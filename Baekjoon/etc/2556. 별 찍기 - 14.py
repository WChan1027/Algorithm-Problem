# https://www.acmicpc.net/problem/2556
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())

sky = [['*'] * N for _ in range(N)]

for stars in sky:
    print(''.join(stars))