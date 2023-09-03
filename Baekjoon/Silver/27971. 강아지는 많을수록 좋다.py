# https://www.acmicpc.net/problem/27971
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M, A, B = map(int, input().split())

cnt = [0] * (N+1)

for i in range(M):
    start, end = map(int, input().split())

    cnt[start:end+1] = [-1] * (end - start + 1)

stack = [0]
num = [A, B]
num.sort(reverse=True)

while stack:
    now = stack.pop(0)

    for i in num:
        if now + i < N:
            if cnt[now + i] == 0 or cnt[now + i] > cnt[now] + 1:
                cnt[now + i] = cnt[now] + 1
                stack.append(now + i)

        elif now + i == N:
            cnt[N] = cnt[now] + 1
            stack = []
            break

if cnt[N] == 0:
    print(-1)
else:
    print(cnt[N])