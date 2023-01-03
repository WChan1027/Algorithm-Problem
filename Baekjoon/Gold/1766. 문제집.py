# https://www.acmicpc.net/problem/1766
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())

problem = list([[]] for _ in range(N+1))
visited = [0] * (N+1)

def check(n):
    print(n, end=' ')
    for i in problem[n][0]:
        problem[i].remove(n)
        if len(problem[i]) == 1 and visited[i] == 0:
            if i < n:
                visited[i] = 1
                check(i)
            else:


for _ in range(M):
    A, B = map(int, input().split())
    problem[A][0].append(B)
    problem[B].append(A)

for i in range(1, N+1):
    problem[i][0].sort()

for num in range(1, N+1):
    if len(problem[num]) > 1:
        pass
    else:
        if visited[num] == 0:
            visited[num] = 1
            check(num)