# https://www.acmicpc.net/problem/11725
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
tree = [list() for _ in range(N+1)]

for _ in range(N-1):
    A, B = map(int, input().split())
    tree[A].append(B)
    tree[B].append(A)

visited = [0] * (N+1)
stack = [1]

while stack:
    now = stack.pop()
    for next in tree[now]:
        if visited[next] == 0:
            visited[next] = now
            stack.append(next)

for answer in visited[2 : N+2]:
    print(answer)