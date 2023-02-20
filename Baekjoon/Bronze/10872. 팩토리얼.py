# https://www.acmicpc.net/problem/10872
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())

answer = 1
for i in range(1, N+1):
    answer *= i

print(answer)