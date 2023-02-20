# https://www.acmicpc.net/problem/15657
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
num = sorted(list(map(int, input().split())))

def answer(n, m, array):
    if n == M:
        print(*array)
        return

    for i in range(m, N):
        answer(n + 1, i, array + [num[i]])

answer(0, 0, [])