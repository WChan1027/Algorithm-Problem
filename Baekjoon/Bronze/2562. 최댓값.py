# https://www.acmicpc.net/problem/2562

answer = 0
for i in range(1, 10):
    N = int(input())
    if N > answer:
        answer = N
        idx = i

print(answer)
print(idx)