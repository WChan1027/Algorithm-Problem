# https://www.acmicpc.net/problem/14425
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
S = []
answer = 0

for _ in range(N):
    S.append(input().strip())

for _ in range(M):
    string = input().strip()

    if string in S:
        answer += 1

print(answer)