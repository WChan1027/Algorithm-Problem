import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())

cards = list(range(N - (N % 2), 0, -2)) + list(range(1, (N+1), 2))
orders = [0] * N

orders[0] = N//2 + 1
for i in range(1, N):
    orders[i] = orders[i-1] + i * ((-1) ** i)

print('YES')
print(*cards)
print(*orders)