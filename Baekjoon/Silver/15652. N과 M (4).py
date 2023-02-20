# https://www.acmicpc.net/problem/15652
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())

def answer(n, m, array):
    if n == M:
        print(*array)
        return

    for i in range(m, N+1):
        answer(n + 1, i, array + [i])

answer(0, 1, [])