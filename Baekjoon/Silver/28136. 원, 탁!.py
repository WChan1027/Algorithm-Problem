import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())

a = list(map(int, input().split()))

cnt = 0
for num in range(N-1):
    if a[num+1] <= a[num]:
        cnt += 1

if a[-1] >= a[0]:
    cnt += 1

print(cnt)