import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, K = map(int, input().split())
diff = []

for i in range(N):
    Moloco, max = map(int, input().split())
    if Moloco < max:
        diff.append(max - Moloco)
    else:
        K -= 1

if K > 0:
    diff.sort()
    answer = diff[K-1]
else:
    answer = 0

print(answer)