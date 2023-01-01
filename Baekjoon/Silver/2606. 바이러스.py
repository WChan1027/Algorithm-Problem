# https://www.acmicpc.net/problem/2606
import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

N = int(input())
M = int(input())

computer = [[0] * (N+1) for _ in range(N+1)]
visited = [0] * (N+1)

for _ in range(M):
    x, y = map(int, input().split())
    computer[x][y] = 1
    computer[y][x] = 1

stack = [1]
visited[1] = 1

while stack:
    now = stack.pop()
    for next in range(1, N+1):
        if computer[now][next] == 1 and visited[next] == 0:
            stack.append(next)
            visited[next] = 1

print(visited.count(1) - 1)