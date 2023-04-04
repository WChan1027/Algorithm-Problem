# https://www.acmicpc.net/problem/2292

N = int(input())

num = 1
n = 0
while num < N:
    n += 1
    num += n*6

print(n+1)