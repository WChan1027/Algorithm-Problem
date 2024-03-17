# https://www.acmicpc.net/problem/1758
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())

def sum_num(num):
    result = 0
    for i in range(1, num+1):
        result += i

    return result

tip = [0] * N
for i in range(N):
    tip[i] = int(input())

tip.sort(reverse=True)

idx = -1
for i in range(N):
    if tip[i] <= i:
        break
    idx += 1

answer = sum(tip[:idx+1]) - sum_num(idx)
print(answer)