import sys
from collections import deque
sys.stdin = open('input.txt')

N, K = map(int, sys.stdin.readline().split())

if N >= K:
    answer = N - K

else:
    visited = [-1 for _ in range(100001)]
    visited[N] = 0
    queue = deque()
    queue.append((N, 0))
    answer = 0

    while not answer:
        now, time = queue.popleft()
        next = [now + 1, now - 1, now * 2]
        for i in next:
            if i == K:
                answer = time + 1
                break

            elif 0 <= i <= 100000 and visited[i] == -1:
                queue.append((i, time + 1))
                visited[i] = time + 1

print(answer)