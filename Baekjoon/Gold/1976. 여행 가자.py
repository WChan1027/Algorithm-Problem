# https://www.acmicpc.net/problem/1976
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())

M = int(input())

city = [list(map(int, input().split())) for _ in range(N)]

plan = list(map(int, input().split()))

stack = [plan[0]-1]
visited = [0] * N
visited[plan[0]-1] = 1
while stack:
    now = stack.pop()

    for next in range(N):
        if city[now][next] == 1 and visited[next] == 0:
            stack.append(next)
            visited[next] = 1

answer = 'YES'
for i in plan:
    if visited[i-1] == 0:
        answer = 'NO'
        break

print(answer)