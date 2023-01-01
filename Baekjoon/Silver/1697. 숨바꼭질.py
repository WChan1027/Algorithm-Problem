# https://www.acmicpc.net/problem/1697
import sys
from collections import deque
sys.stdin = open('input.txt')


N, K = map(int, sys.stdin.readline().split())

if N >= K:
    print(N - K)

else:
    time = [-1] * 100001

    stack = deque()
    stack.append(N)
    time[N] = 0

    while stack:
        locate = stack.popleft()

        if locate == K:
            break

        next_locate = locate * 2
        if 0 < next_locate <= 100000 and time[next_locate] == -1:
            time[next_locate] = time[locate] + 1
            stack.appendleft(next_locate)

        next_locate = locate - 1
        if 0 <= next_locate <= 100000 and time[next_locate] == -1:
            time[next_locate] = time[locate] + 1
            stack.append(next_locate)

        next_locate = locate + 1
        if 0 <= next_locate <= 100000 and time[next_locate] == -1:
            time[next_locate] = time[locate] + 1
            stack.append(next_locate)

    print(time[K])