import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
planned_page = list(map(int, input().split()))
studied_page = list(map(int, input().split()))

answer = 0
for day in range(N):
    answer += 1 if planned_page[day] <= studied_page[day] else 0

print(answer)