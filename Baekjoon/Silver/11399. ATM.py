# https://www.acmicpc.net/problem/11399
import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())

line = list(map(int, sys.stdin.readline().split()))

line.sort(reverse=True)

time = 0
for t in range(N):
    time += (t+1) * line[t]

print(time)