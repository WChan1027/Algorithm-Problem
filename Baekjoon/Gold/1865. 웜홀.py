# https://www.acmicpc.net/problem/1865
import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline

TC = int(input())

for test_case in range(TC):
    N, M, W = map(int, input().split())

    road = [[0] * (N+1) for _ in range(N+1)]
    yes = 0

    for _ in range(M):
        S, E, T = map(int, input().split())
        if road[S][E] == 0 or road[S][E] > T:
            road[S][E] = T
        if road[E][S] == 0 or road[E][S] > T:
            road[E][S] = T

    for _ in range(W):
        S, E, T = map(int, input().split())
        if road[S][E] == 0 or road[S][E] > -T:
            road[S][E] = -T

    time = [100000000] * (N+1)

    for _ in range(1, N+1):
        for i in range(1, N+1):
            for j in range(1, N+1):
                if road[i][j] != 0:
                    if time[j] > time[i] + road[i][j]:
                        time[j] = time[i] + road[i][j]

    for i in range(1, N+1):
        for j in range(1, N+1):
            if road[i][j] != 0 and time[j] > time[i] + road[i][j]:
                yes = 1
                break
        if yes == 1:
            break

    if yes == 1:
        print('YES')
    else:
        print('NO')