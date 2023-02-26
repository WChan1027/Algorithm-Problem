# https://www.acmicpc.net/contest/problem/956/3
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())

lst = list(map(int, input().split()))

count = dict()
for num in lst:
    if num != 0:
        if num in count.keys():
            count[num] += 1
        else:
            count[num] = 1

flag = 1
while flag == 1:
    flag = 0
    sorted_count = dict(sorted(count.items()))

    for key in sorted_count.keys():
        up = count[key] // 2
        if up > 0:
            flag = 1
            if key * 2 in count.keys():
                count[key] -= up * 2
                count[key * 2] += up
            else:
                count[key] -= up * 2
                count[key * 2] = up

print(sorted(count.keys())[-1])