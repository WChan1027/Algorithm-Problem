import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
eps = 1e-9
if n == 0:
    answer = 0
else:
    num = sorted([int(input()) for _ in range(n)])
    ex = round(n*0.15 + eps)
    num = num[ex:n-ex]
    answer = round(sum(num) / len(num) + eps)

print(answer)