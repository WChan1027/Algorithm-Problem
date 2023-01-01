# https://www.acmicpc.net/problem/20159
import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())

card = list(map(int, sys.stdin.readline().split()))

card_sum = [0] * N
sum_trick = [0] * N

total = 0
for i in range(N):
    if i % 2 == 0:
        total += card[i]
    card_sum[i] = total

total = 0
for i in range(N-1, -1, -1):
    if i % 2 == 1:
        total += card[i]
    sum_trick[i] = total

answer = card_sum[-1]
result = sum_trick[0]
if answer < result:
    answer = result

for i in range(N-2):
    result = card_sum[i] + sum_trick[i+1] - sum_trick[-1]
    if answer < result:
        answer = result
    result = card_sum[i] + sum_trick[i+2]
    if answer < result:
        answer = result

print(answer)