'''
https://www.acmicpc.net/problem/1260

[문제]

그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오.
단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다.
정점 번호는 1번부터 N번까지이다.

'''
import sys
from collections import deque
sys.stdin = open('input.txt')

N, M, V = map(int, sys.stdin.readline().split())
matrix = [[0]*(N+1) for _ in range(N+1)]

DFS = []
BFS = []

for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    matrix[x][y] = 1
    matrix[y][x] = 1

stack = []
visited = [0]*(N+1)
stack.append(V)
while stack:
    a = stack.pop()
    if visited[a] == 0:
        visited[a] = 1
        DFS.append(a)
        for i in range(N, 0, -1):
            if matrix[a][i] == 1 and visited[i] == 0:
                stack.append(i)


stack = []
visited = [0]*(N+1)
stack.append(V)
visited[V] = 1
while stack:
    a = stack.pop(0)
    BFS.append(a)
    for i in range(N+1):
        if matrix[a][i] == 1 and visited[i] == 0:
            stack.append(i)
            visited[i] = 1

print(*DFS)
print(*BFS)