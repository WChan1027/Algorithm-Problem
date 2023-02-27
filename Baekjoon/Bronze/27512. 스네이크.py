# https://www.acmicpc.net/contest/problem/956/1
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n, m = map(int, input().split())

if (n * m) % 2 == 1:
    print(n * m - 1)
else:
    print(n * m)