import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())

x, y = map(int, input().split())

cnt = 4
if x == 1:
    cnt -= 1
if x == N:
    cnt -= 1
if y == 1:
    cnt -= 1
if y == N:
    cnt -= 1

print(cnt)