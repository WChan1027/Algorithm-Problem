# https://www.acmicpc.net/problem/2525
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

A, B = map(int, input().split())
C = int(input())

B += C

if B >= 60:
    A += B // 60
    B %= 60

if A >= 24:
    A %= 24

print(A, B)