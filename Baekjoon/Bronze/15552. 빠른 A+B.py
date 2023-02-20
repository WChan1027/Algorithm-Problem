# https://www.acmicpc.net/problem/15552
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

T = int(input())

for test_case in range(T):
    A, B = map(int, input().split())
    print(A+B)