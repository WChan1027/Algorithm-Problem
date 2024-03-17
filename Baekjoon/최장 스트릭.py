import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
solved = list(map(int, input().split()))

cnt = 0
answer = 0
for case in solved:
    if case == 0:
        answer = max(answer, cnt)
        cnt = 0
    else:
        cnt += 1

answer = max(answer, cnt)

print(answer)