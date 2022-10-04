import sys
sys.stdin = open('sample_input.txt')
from collections import deque

def min_time():
    Q = deque()
    Q.append(0)
    while Q:
        a = Q.popleft()
        for i in range(N+1):
            if road[a][i] != 0:
                if time[i] == 0:
                    time[i] = time[a] + road[a][i]
                    Q.append(i)
                elif time[i] > time[a] + road[a][i]:
                    time[i] = time[a] + road[a][i]
                    Q.append(i)


T = int(input())

for test_case in range(1, T+1):
    N, E = map(int, input().split())
    road = [[0]*(N+1) for _ in range(N+1)]

    for _ in range(E):
        a = list(map(int, input().split()))
        road[a[0]][a[1]] = a[2]

    time = [0] * (N+1)

    min_time()

    print(f'#{test_case} {time[N]}')