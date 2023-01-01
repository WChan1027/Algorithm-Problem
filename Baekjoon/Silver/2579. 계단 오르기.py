# https://www.acmicpc.net/problem/2579
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())

stair = [0] * (N+1)
for i in range(1, N+1):
    stair[i] = int(input())

point = list([0] * (N+1) for _ in range(3))

def result(now, count, score):
    global answer
    if now > 0:
        if point[count][now] < score:
            point[count][now] = score
        else:
            return

    if now == N:
        if answer < score:
            answer = score
        return

    if count == 2:
        if now+2 <= N:
            result(now+2, 1, score + stair[now+2])
    else:
        result(now+1, count+1, score + stair[now+1])
        if now+2 <= N:
            result(now+2, 1, score + stair[now+2])

answer = 0
result(0, 0, 0)

print(answer)