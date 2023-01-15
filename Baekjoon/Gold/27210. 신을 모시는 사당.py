# https://www.acmicpc.net/problem/27210
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
statue = list(map(int, input().split()))

a = []

cnt = 0
dir = statue[0]
for i in range(N):
    if statue[i] == 1:
        if dir == 2:
            a.append(cnt)
            dir = 1
            cnt = 1
        else:
            cnt += 1

    else:
        if dir == 1:
            a.append(cnt)
            dir = 2
            cnt = -1
        else:
            cnt -= 1

a.append(cnt)

answer1 = 0
if a[0] > 0:
    for i in range(0, len(a), 2):
        b = a[i]
        idx = i

        result = 0
        for j in range(1, len(a) - idx):
            result += a[idx + j]
            if result > 0:
                b += result
                result = 0

        if b > answer1:
            answer1 = b
else:
    for i in range(1, len(a), 2):
        b = a[i]
        idx = i

        result = 0
        for j in range(1, len(a) - idx):
            result += a[idx + j]
            if result > 0:
                b += result
                result = 0

        if b > answer1:
            answer1 = b


answer2 = 0
if a[0] < 0:
    for i in range(0, len(a), 2):
        b = a[i]
        idx = i

        result = 0
        for j in range(1, len(a) - idx):
            result += a[idx + j]
            if result < 0:
                b += result
                result = 0

        if b < answer2:
            answer2 = b
else:
    for i in range(1, len(a), 2):
        b = a[i]
        idx = i

        result = 0
        for j in range(1, len(a) - idx):
            result += a[idx + j]
            if result < 0:
                b += result
                result = 0

        if b < answer2:
            answer2 = b

print(max(answer1, -answer2))




# answer = max(a)
#
# idx = a.index(max(a))
#
# result = 0
# for i in range(1, idx+1):
#     result += a[idx - i]
#     if result > 0:
#         answer += result
#         result = 0
#
# result = 0
# for i in range(1, len(a) - idx):
#     result += a[idx + i]
#     if result > 0:
#         answer += result
#         result = 0
#
# print(answer)

# for i in range(len(a)-1):
#     for j in range(i+1, len(a)):
#         if sum(a[i:j]) > answer:
#             answer = sum(a[i:j])
#
# print(answer)