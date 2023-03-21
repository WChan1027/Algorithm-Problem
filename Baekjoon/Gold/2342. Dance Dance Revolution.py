# https://www.acmicpc.net/problem/2342
import sys
from collections import defaultdict
sys.stdin = open('input.txt')
input = sys.stdin.readline

order = list(map(int, input().split()))
score = [defaultdict(list) for _ in range(len(order)-1)]

n = 0

while True:
    # 종료
    if order[n] == 0:
        break

    # 처음 / 두 발이 0에 있을 때
    # 발: (0, order[0])
    if n == 0:
        score[n][0] = 2

    else:
        # 발: (key, order[n-1])
        for key in score[n-1].keys():
            # 한 발이 0에 있을 때
            if key == 0:
                # 나머지 발 order[n-1]이 눌러야 될 발판 order[n]에 있을 때
                # 발: (0, order[n])
                if order[n-1] == order[n]:
                    if key in score[n].keys():
                        score[n][key] = min(score[n][key], score[n-1][key] + 1)
                    else:
                        score[n][key] = score[n-1][key] + 1

                # 나머지 발 order[n-1]이 눌러야 될 발판 order[n]에 없을 때
                else:
                    # 나머지 발 order[n-1]로 order[n]을 밟을 때
                    # 발: (0, order[n])
                    if key in score[n].keys():
                        if order[n] + order[n - 1] == 4 or order[n] + order[n - 1] == 6:
                            score[n][key] = min(score[n][key], score[n - 1][key] + 4)
                        else:
                            score[n][key] = min(score[n][key], score[n - 1][key] + 3)
                    else:
                        if order[n] + order[n - 1] == 4 or order[n] + order[n - 1] == 6:
                            score[n][key] = score[n - 1][key] + 4
                        else:
                            score[n][key] = score[n - 1][key] + 3

                    # 0에 있는 발로 order[n]을 밟을 때
                    # 발: (order[n-1], order[n])
                    if order[n - 1] in score[n].keys():
                        score[n][order[n - 1]] = min(score[n][order[n - 1]], score[n - 1][key] + 2)
                    else:
                        score[n][order[n - 1]] = score[n - 1][key] + 2

            # 한 발이 밟아야 하는 발판 order[n]에 있을 때
            # 발: (order[n], order[n-1])
            elif key == order[n]:
                if order[n-1] in score[n].keys():
                    score[n][order[n-1]] = min(score[n][order[n-1]], score[n - 1][key] + 1)
                else:
                    score[n][order[n-1]] = score[n - 1][key] + 1

            # 한 발이 밟아야 하는 발판 order[n]에 있을 때
            # 발: (key, order[n-1])
            elif order[n] == order[n-1]:
                if key in score[n].keys():
                    score[n][key] = min(score[n][key], score[n - 1][key] + 1)
                else:
                    score[n][key] = score[n - 1][key] + 1

            # 두 발 모두 0에 없고, 밟아야 하는 발판 order[n]에 없을 때
            else:
                # order[n-1]에 있는 발로 order[n]을 밟을 때
                # 발: (key, order[n])
                if key in score[n].keys():
                    if order[n] + order[n-1] == 4 or order[n] + order[n-1] == 6:
                        score[n][key] = min(score[n][key], score[n-1][key] + 4)
                    else:
                        score[n][key] = min(score[n][key], score[n-1][key] + 3)

                else:
                    if order[n] + order[n-1] == 4 or order[n] + order[n-1] == 6:
                        score[n][key] = score[n - 1][key] + 4
                    else:
                        score[n][key] = score[n - 1][key] + 3

                # key에 있는 발로 order[n]을 밟을 때
                # 발: (order[n], order[n-1])
                if order[n-1] in score[n].keys():
                    if order[n] + key == 4 or order[n] + key == 6:
                        score[n][order[n-1]] = min(score[n][order[n-1]], score[n - 1][key] + 4)
                    else:
                        score[n][order[n-1]] = min(score[n][order[n-1]], score[n - 1][key] + 3)

                else:
                    if order[n] + key == 4 or order[n] + key == 6:
                        score[n][order[n-1]] = score[n - 1][key] + 4
                    else:
                        score[n][order[n-1]] = score[n - 1][key] + 3

    n += 1

if len(order) == 1:
    print(0)
else:
    print(min(score[n-1].values()))
