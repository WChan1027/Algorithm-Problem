# https://www.acmicpc.net/problem/17128
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, Q = map(int, input().split())

score = list(map(int, input().split()))
num = list(map(int, input().split()))

scores = [0] * N
scores[N-3] = score[N-3] * score[N-2] * score[N-1] * score[0]
scores[N-2] = score[N-2] * score[N-1] * score[0] * score[1]
scores[N-1] = score[N-1] * score[0] * score[1] * score[2]

for i in range(N-3):
    scores[i] = score[i] * score[i+1] * score[i+2] * score[i+3]

S = sum(scores)

for idx in num:
    for i in range(4):
        scores[idx-1] *= -1
        S += 2*scores[idx-1]
        idx -= 1
        if idx < 1:
            idx += N
    print(S)