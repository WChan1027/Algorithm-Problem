# https://www.acmicpc.net/problem/1463
import sys
from collections import deque
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())

results = [N] * (N+1)

stack = deque()
stack.append(N)
results[N] = 0
while stack:
    n = stack.popleft()
    if n % 3 == 0:
        if results[n//3] > results[n] + 1:
            results[n//3] = results[n] + 1
            stack.append(n//3)
    if n % 2 == 0:
        if results[n//2] > results[n] + 1:
            results[n//2] = results[n] + 1
            stack.append(n//2)
    if results[n-1] > results[n] + 1:
        results[n-1] = results[n] + 1
        stack.append(n-1)

print(results[1])