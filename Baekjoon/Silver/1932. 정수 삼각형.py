# https://www.acmicpc.net/problem/1932
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())

triangle = [list(map(int, input().split())) for _ in range(N)]

visited = [[0] * i for i in range(1, N+1)]

for i in range(N):
    for j in range(i+1):
        if j == 0:
            visited[i][0] = visited[i-1][0] + triangle[i][0]
        elif j == i:
            visited[i][i] = visited[i-1][i-1] + triangle[i][i]
        else:
            visited[i][j] = max(visited[i-1][j-1], visited[i-1][j]) + triangle[i][j]

print(max(visited[N-1]))


# def calc(line, idx, result):
#     if line == N-1:
#         return
#
#     if result + triangle[line+1][idx] > visited[line+1][idx]:
#         visited[line+1][idx] = result + triangle[line+1][idx]
#         calc(line + 1, idx, result + triangle[line+1][idx])
#
#     if result + triangle[line+1][idx+1] > visited[line+1][idx+1]:
#         visited[line+1][idx+1] = result + triangle[line+1][idx+1]
#         calc(line + 1, idx+1, result + triangle[line+1][idx+1])
#
# calc(0, 0, triangle[0][0])
# print(max(visited[N-1]))