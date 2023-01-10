# https://www.acmicpc.net/problem/1389
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())

relation = [[0] * (N+1) for _ in range(N+1)]

for _ in range(M):
    A, B = map(int, input().split())
    relation[A][B] = 1
    relation[B][A] = 1

result = [0] * (N+1)

for i in range(1, N+1):
    que = [i]
    visited = [N] * (N+1)
    visited[0] = visited[i] = 0
    while que:
        A = que.pop()
        for j in range(1, N+1):
            if relation[A][j] == 1 and visited[j] > visited[A] + 1:
                visited[j] = visited[A] + 1
                que.append(j)
    result[i] = sum(visited)

print(result.index(min(result[1:])))