import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())

lagrangian = [0] * (n+1)

for i in range(1, 224):
    lagrangian[i**2] = 1

cnt = 0
while lagrangian[n] == 0:
    cnt += 1
    for i in range(1, n):
        if lagrangian[i] == cnt:
            for j in range(1, 224):
                if i + j**2 <= n:
                    if lagrangian[i + j**2] == 0:
                        lagrangian[i + j**2] = cnt + 1
                else:
                    break
        if lagrangian[n] != 0:
            break

print(lagrangian[n])