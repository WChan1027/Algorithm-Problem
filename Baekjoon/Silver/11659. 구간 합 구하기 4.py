import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())

num = list(map(int, input().split()))

num_sum = [0]

for i in num:
    num_sum.append(num_sum[-1] + i)

for _ in range(M):
    i, j = map(int, input().split())
    print(num_sum[j] - num_sum[i - 1])