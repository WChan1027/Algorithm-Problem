# https://www.acmicpc.net/problem/11403
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())

graph = list(list(map(int, input().split())) for _ in range(N))

answer = list([0] * N for _ in range(N))

stack = []
for i in range(N):
    stack.append(i)
    visited = [0] * N

    while stack:
        a = stack.pop()

        for j in range(N):
            if graph[a][j] == 1 and visited[j] == 0:
                stack.append(j)
                visited[j] = 1
                answer[i][j] = 1

for line in answer:
    print(*line)