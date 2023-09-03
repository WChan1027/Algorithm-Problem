import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())

cnt = 0
num = 0
while num < N:
    num = 2 ** cnt

    cnt += 1

print(cnt)