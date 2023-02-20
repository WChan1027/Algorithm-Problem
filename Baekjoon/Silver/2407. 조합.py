# https://www.acmicpc.net/problem/2407
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n, m = map(int, input().split())

A, B = 1, 1

for i in range(1, m+1):
    A *= (n-i+1)
    B *= i

print(A // B)