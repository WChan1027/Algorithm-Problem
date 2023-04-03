import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())

score = {'D': 0, 'P': 0}

for round in range(N):
    win = input().strip()

    score[win] += 1

    if abs(score['D'] - score['P']) == 2:
        break

print(f"{score['D']}:{score['P']}")