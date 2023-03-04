# https://www.acmicpc.net/problem/10430
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

A, B, C = map(int, input().split())

print((A + B) % C)
print(((A % C) + (B % C)) % C)
print((A * B) % C)
print(((A % C) * (B % C)) % C)