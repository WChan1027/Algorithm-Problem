# https://www.acmicpc.net/problem/15654
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
num = sorted(list(map(int, input().split())))
visited = [0] * N
def answer(n, array):
    if n == M:
        print(*array)
        return

    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            answer(n + 1, array + [num[i]])
            visited[i] = 0

answer(0, [])