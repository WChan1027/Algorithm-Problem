# https://www.acmicpc.net/problem/2096
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())

max_tmp = [0] * 3
min_tmp = [0] * 3
max_num = [0] * 3
min_num = [0] * 3
for _ in range(N):
    a, b, c = map(int, input().split())

    for i in range(3):
        if i == 0:
            max_num[i] = a + max(max_tmp[0], max_tmp[1])
            min_num[i] = a + min(min_tmp[0], min_tmp[1])
        elif i == 1:
            max_num[i] = b + max(max_tmp[0], max_tmp[1], max_tmp[2])
            min_num[i] = b + min(min_tmp[0], min_tmp[1], min_tmp[2])
        else:
            max_num[i] = c + max(max_tmp[1], max_tmp[2])
            min_num[i] = c + min(min_tmp[1], min_tmp[2])

    for i in range(3):
        max_tmp[i] = max_num[i]
        min_tmp[i] = min_num[i]

print(max(max_num), min(min_num))