import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())

bus = list(tuple(map(int, input().split())) for _ in range(M))
time = [float('INF')] * N
time[0] = 0
answer = 0

# 벨만-포드
for i in range(N):
    for j in range(M):
        (s, e, t) = bus[j]
        if time[e-1] > time[s-1] + t:
            if i == N-1:
                answer = -1
            time[e-1] = time[s-1] + t

if not answer:
    for result in time[1:]:
        print(result if result != float('INF') else -1)
else:
    print(answer)
