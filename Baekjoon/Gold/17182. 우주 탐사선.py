# https://www.acmicpc.net/problem/17182
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, K = map(int, input().split())

time = [list(map(int, input().split())) for _ in range(N)]

def Floyd_Warshall():
    min_time = [[1000*N] * N for _ in range(N)]

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
answer = 0

while len(set(visited)) > 1:
    answer += min(min_time[K])
    visited[min_time.index(min(min_time[K]))] = 1


print(answer)