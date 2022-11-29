# https://www.acmicpc.net/problem/5525
import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
S = sys.stdin.readline()

idx = 0
count = 0
answer = 0
while idx < len(S) - 3:
    if S[idx:idx+3] == 'IOI':
        count += 1
        idx += 2
        if count == N:
            answer += 1
            count -= 1
    else:
        idx += 1
        count = 0

print(answer)