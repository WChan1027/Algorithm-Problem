# https://www.acmicpc.net/problem/2231

N = input()

answer = 0
for i in range(1, int(N)):
    num = i
    for j in str(i):
        num += int(j)
    if num == int(N):
        answer = i
        break

print(answer)