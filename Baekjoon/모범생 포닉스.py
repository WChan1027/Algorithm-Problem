import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())

plan = list(map(int, input().split()))

time = (N-1) * 8 + sum(plan)

print(f'{time // 24} {time % 24}')