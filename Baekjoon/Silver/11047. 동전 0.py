import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, K = map(int, input().split())

price = [int(input()) for _ in range(N)]

cnt = 0
idx = len(price) - 1
while K > 0:
    if price[idx] <= K:
        K -= price[idx]
        cnt += 1
    else:
        idx -= 1

print(cnt)