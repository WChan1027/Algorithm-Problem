import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

x, N = map(int, input().split())
case1 = [0, 6, 5, 12]
case2 = [8, 2, 7]

for t in range(N):
    if x % 2:
        x = int(bin(x*2 ^ 6), 2)
    else:
        x = int(bin(x//2 ^ 6), 2)

    if x == 4:
        x = 4
        break

    elif x == 0:
        x = case1[(N-1 - t) % 4]
        break

    elif x == 8:
        x = case2[(N-1 -t) % 3]
        break

print(x)