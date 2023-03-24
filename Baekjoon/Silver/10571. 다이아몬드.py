# https://www.acmicpc.net/problem/10571
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

T = int(input())

for test_case in range(T):
    N = int(input())
    diamonds = [(0, 0)] * N
    cnt = [1] * N
    for idx in range(N):
        w, c = map(float, input().split())
        for diamond in range(idx):
            if diamonds[diamond][0] < w and diamonds[diamond][1] > c:
                cnt[idx] = max(cnt[idx], cnt[diamond] + 1)
        diamonds[idx] = (w, c)

    print(max(cnt))