# https://www.acmicpc.net/problem/1321
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())

soldiers = list(map(int, input().split()))

num = [0] * N
num[0] = soldiers[0]
for i in range(1, N):
    num[i] = num[i-1] + soldiers[i]

M = int(input())

for _ in range(M):
    order = list(map(int, input().split()))
    if order[0] == 1:
        for i in range(order[1] - 1, N):
            num[i] += order[2]
    else:
        start = 0
        end = N - 1

        while start <= end:
            mid = (start + end) // 2

            if num[mid] < order[1]:
                start = mid + 1
            else:
                end = mid - 1

        print(start + 1)