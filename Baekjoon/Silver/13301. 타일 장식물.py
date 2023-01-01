# https://www.acmicpc.net/problem/13301
import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())

length = [0] * (N+1)

length[0], length[1] = 1, 1

for i in range(2, N+1):
    length[i] = length[i-1] + length[i-2]

answer = 2 * (length[N] + length[N-1])

print(answer)