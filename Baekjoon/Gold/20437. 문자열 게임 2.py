# https://www.acmicpc.net/problem/20437
import sys
from collections import defaultdict
sys.stdin = open('input.txt')
input = sys.stdin.readline

T = int(input())

for test_case in range(T):
    W = input().strip()
    K = int(input())
    cnt = defaultdict(list)

    if K == 1:
        print(1, 1)
        continue

    for i in range(len(W)):
        cnt[W[i]] += [i]

    delete = []

    for i in cnt:
        if len(cnt[i]) < K:
            delete.append(i)

    for i in delete:
        del(cnt[i])

    if not cnt:
        print(-1)
        continue

    min_length = float('inf')
    max_length = 0

    for i in cnt:
        for idx in range(len(cnt[i]) + 1 - K):
            result = cnt[i][idx + K - 1] - cnt[i][idx] + 1

            min_length = min(min_length, result)
            max_length = max(max_length, result)

    print(min_length, max_length)