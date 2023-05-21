import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())

tree = list(map(int, input().split()))

answer = 0
idx = N
for lemon in tree:
    lemon -= idx
    answer = max(answer, lemon)
    idx -= 1

print(answer)