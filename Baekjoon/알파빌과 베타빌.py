import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())

waiting = list(map(int, input().split()))

friends = list(map(int, input().split()))

answer = 0

for num in waiting[:M]:
    if num not in friends:
        answer += 1

print(answer)