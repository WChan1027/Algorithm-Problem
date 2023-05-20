# https://www.acmicpc.net/problem/11265
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())

party = [list(map(int, input().split())) for _ in range(N)]

# 플로이드-워셜
def Floyd_Warshall():
    # 경유지점
    for k in range(N):
        # 출발지점
        for i in range(N):
            # 도착지점
            for j in range(N):
                # 출발지점에서 도착지점까지 가는 가장 빠른 시간을 갱신
                party[i][j] = min(party[i][j], party[i][k] + party[k][j])

Floyd_Warshall()
for guest in range(M):
    A, B, C = map(int, input().split())

    if party[A-1][B-1] <= C:
        print('Enjoy other party')
    else:
        print('Stay here')