import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

score_A = [0] * 10
score_B = [0] * 10

A, B = map(int, input().split())

C = 0

cnt = 9
while cnt >= 0:
    num = 2 ** cnt

    if A >= num:
        score_A[cnt] = 1
        A -= num

    if B >= num:
        score_B[cnt] = 1
        B -= num

    cnt -= 1

for idx in range(10):
    cnt = 0
    if score_A[idx] == 1:
        cnt += 1

    if score_B[idx] == 1:
        cnt += 1

    if cnt == 1:
        C += 2 ** idx


print(C)