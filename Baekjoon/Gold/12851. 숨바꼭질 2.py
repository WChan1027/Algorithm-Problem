# https://www.acmicpc.net/problem/12851
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, K = map(int, input().split())

time = [0] * 100001

stack = [N]
min_time = 100000
cnt = 0

while stack:
    now = stack.pop()
    if now > K:
        if min_time > time[now] + (now - K):
            min_time = time[now] + (now - K)
            cnt = 1
        elif min_time == time[now] + (now - K):
            cnt += 1

    elif now == K:
        if time[now] < min_time:
            cnt = 1
            min_time = time[now]
        elif time[now] == min_time:
            cnt += 1

    else:
        if time[now] < min_time:
            for next in [now+1, now-1, now*2]:
                if 0 <= next <= 100000:
                    if time[next] == 0 or time[next] >= time[now] + 1:
                        time[next] = time[now] + 1
                        stack.append(next)

print(min_time)
print(cnt)