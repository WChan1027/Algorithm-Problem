# https://www.acmicpc.net/problem/23762
import sys
# import itertools
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())

npc = N % 4

skill = list(map(int, input().split()))
skill_idx = dict()
for i in range(N):
    skill_idx[skill[i]] = i

skill = sorted(skill)

dp = [[float('INF')] + [-1] * npc for _ in range(N)]
dp[0][0], dp[1][0], dp[2][0], dp[3][0] = 0, 0, 0, skill[3] - skill[0]

for i in range(3, N):
    a = (i+1) % 4

    if a <= npc:
        if a == 0:
            if i < 4:
                dp[i][0] = min(dp[i][0], dp[0][0] + skill[i] - skill[i - 3])
            else:
                dp[i][0] = min(dp[i][0], dp[i-4][0] + skill[i] - skill[i-3])

        elif a == 1:
            if i < 5:
                dp[i][0] = min(dp[i][0], dp[i-4][0] + skill[i] - skill[i - 3], dp[0][0] + skill[i] - skill[i - 3])
                if dp[i][0] == dp[i - 4][0] + skill[i] - skill[i - 3]:
                    dp[i][1] = i - 4

                elif dp[i][0] == dp[i - 5][0] + skill[i] - skill[i - 3]:
                    dp[i][1] = i - 4
            else:
                dp[i][0] = min(dp[i][0], dp[i-4][0] + skill[i] - skill[i-3], dp[i-5][0] + skill[i] - skill[i-3])
                if dp[i][0] == dp[i-5][0] + skill[i] - skill[i-3]:
                    dp[i][1] = i-4

        elif a == 2:
            if i < 6:
                dp[i][0] = min(dp[i][0], dp[i - 4][0] + skill[i] - skill[i - 3], dp[i - 5][0] + skill[i] - skill[i - 3],
                               dp[0][0] + skill[i] - skill[i - 3])
                if dp[i][0] == dp[i - 5][0] + skill[i] - skill[i - 3]:
                    dp[i][1] = 0
                elif dp[i][0] == dp[i - 6][0] + skill[i] - skill[i - 3]:
                    dp[i][1] = 0
                    dp[i][2] = 1
            else:
                dp[i][0] = min(dp[i][0], dp[i-4][0] + skill[i] - skill[i-3], dp[i-5][0] + skill[i] - skill[i-3], dp[i-6][0] + skill[i] - skill[i-3])
                if dp[i][0] == dp[i-5][0] + skill[i] - skill[i-3]:
                    dp[i][1] = dp[i-5][1]
                    dp[i][2] = i-4
                elif dp[i][0] == dp[i-6][0] + skill[i] - skill[i-3]:
                    dp[i][1] = i-5
                    dp[i][2] = i-4

        else:
            if i < 7:
                dp[i][0] = min(dp[i][0], dp[i-4][0] + skill[i] - skill[i-3], dp[i-5][0] + skill[i] - skill[i-3], dp[i-6][0] + skill[i] - skill[i-3], dp[0][0] + skill[i] - skill[i-3])
                if dp[i][0] == dp[i-5][0] + skill[i] - skill[i-3]:
                    dp[i][1] = 0
                elif dp[i][0] == dp[i-6][0] + skill[i] - skill[i-3]:
                    dp[i][1] = 0
                    dp[i][2] = 1
                elif dp[i][0] == dp[i-7][0] + skill[i] - skill[i-3]:
                    dp[i][1] = 0
                    dp[i][2] = 1
                    dp[i][3] = 2
            else:
                dp[i][0] = min(dp[i][0], dp[i - 4][0] + skill[i] - skill[i - 3], dp[i - 5][0] + skill[i] - skill[i - 3],
                               dp[i - 6][0] + skill[i] - skill[i - 3], dp[i - 7][0] + skill[i] - skill[i - 3])
                if dp[i][0] == dp[i - 5][0] + skill[i] - skill[i - 3]:
                    dp[i][1] = dp[i-5][1]
                    dp[i][2] = dp[i-5][2]
                    dp[i][3] = i - 4
                elif dp[i][0] == dp[i - 6][0] + skill[i] - skill[i - 3]:
                    dp[i][1] = dp[i-6][1]
                    dp[i][2] = i - 5
                    dp[i][3] = i - 4
                elif dp[i][0] == dp[i - 7][0] + skill[i] - skill[i - 3]:
                    dp[i][1] = i - 6
                    dp[i][2] = i - 5
                    dp[i][3] = i - 4

answer = float('INF')
idx = 0
for i in range(-4, 0):
    if dp[i][0] < answer:
        idx = i
        answer = dp[i][0]
print(dp)
print(answer)
cnt = N
for i in range(1, npc+1):
    if dp[idx][i] == -1:
        print(cnt)
        cnt -= 1
    else:
        print(dp[idx][i])
