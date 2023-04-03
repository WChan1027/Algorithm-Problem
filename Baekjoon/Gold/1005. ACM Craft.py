# https://www.acmicpc.net/problem/1005
import sys
from collections import defaultdict, deque
sys.stdin = open('input.txt')
input = sys.stdin.readline

T = int(input())

for test_case in range(T):
    N, K = map(int, input().split())

    time = [0] + list(map(int, input().split()))
    cnt = [0] * (N+1)
    building = defaultdict(list)
    for _ in range(K):
        X, Y = map(int, input().split())
        building[Y].append(X)
        cnt[Y] += 1

    W = int(input())
    que = deque()
    for i in range(1, N + 1):
        if not building[i]:
            que.append(i)
    while que:
        now = que.popleft()
        t = 0

        for next in range(1, N + 1):
            if now in building[next]:
                cnt[next] -= 1
                if cnt[next] == 0:
                    que.append(next)
            if next in building[now]:
                t = max(time[next], t)

        time[now] += t

    print(time[W])