# https://www.acmicpc.net/problem/15650
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())

result = []

def find(a, cnt):
    if cnt == M:
        print(*result)
        return
    for i in range(a+1, N+1):
        result.append(i)
        find(i, cnt+1)
        result.pop()
    return

find(0, 0)