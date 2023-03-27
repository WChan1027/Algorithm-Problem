# https://www.acmicpc.net/problem/2588

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

A = int(input())
B = int(input())

print(A * (B % 10))
print(A * ((B // 10) % 10))
print(A * (B // 100))
print(A * B)