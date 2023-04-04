import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
fibo = [0] * 2
fibo[0], fibo[1] = 1, 1

for i in range(2, N):
    fibo.append(fibo[i-2] + fibo[i-1])

print(fibo[N-1])