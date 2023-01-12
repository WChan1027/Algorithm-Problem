# https://www.acmicpc.net/problem/17182
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, K = map(int, input().split())

time = [list(map(int, input().split())) for _ in range(N)]

def Floyd_Warshall():
    min_time = [[1001*N] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            min_time[i][j] = time[i][j]

    for k in range(N):
        for i in range(N):
            for j in range(N):
                if min_time[i][j] > min_time[i][k] + min_time[k][j]:
                    min_time[i][j] = min_time[i][k] + min_time[k][j]
    return min_time

min_time = Floyd_Warshall()

visited = [0] * N
visited[K] = 1
answer = 1001 * N

def check(now, cnt, result):
    global answer
    if cnt == N:
        if result < answer:
            answer = result
        return

    if result > answer:
        return

    for next in range(N):
        if visited[next] == 0:
            visited[next] = 1
            check(next, cnt + 1, result + min_time[now][next])
            visited[next] = 0

check(K, 1, 0)
print(answer)

# while 0 in visited:
#     short = 1000
#     next = 0
#     for i in range(N):
#         if visited[i] == 0 and 0 <= min_time[K][i] <= short:
#             short = min_time[K][i]
#             next = i
#     answer += short
#     K = next
#     visited[K] = 1
#
# print(answer)