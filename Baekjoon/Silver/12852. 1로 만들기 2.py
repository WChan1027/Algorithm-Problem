# https://www.acmicpc.net/problem/12852
import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())

que = deque()
que.append([N])

while que:
    num = que.popleft()
    if num[0] == 1:
        answer = num
        break

    if num[0] % 3 == 0:
        que.append([num[0]//3] + num)

    if num[0] % 2 == 0:
        que.append([num[0]//2] + num)

    que.append([num[0] - 1] + num)

print(len(answer) -1)
print(*answer[::-1])



# num = [[] for _ in range(N+1)]
#
# def result(n, nums):
#     if n == 1:
#         if num[1]:
#             if len(nums) < len(num[1]):
#                 num[1] = nums
#         else:
#             num[1] = nums
#         return
#
#     if n % 3 == 0:
#         if num[n//3]:
#             if len(num[n//3]) > len(nums) + 1:
#                 num[n//3] = nums + [n//3]
#                 result(n//3, nums + [n//3])
#         else:
#             num[n // 3] = nums + [n // 3]
#             result(n // 3, nums + [n // 3])
#
#     if n % 2 == 0:
#         if num[n//2]:
#             if len(num[n//2]) > len(nums) + 1:
#                 num[n//2] = nums + [n//2]
#                 result(n//2, nums + [n//2])
#         else:
#             num[n // 2] = nums + [n // 2]
#             result(n // 2, nums + [n // 2])
#
#     if n > 1:
#         if num[n-1]:
#             if len(num[n-1]) > len(nums) + 1:
#                 num[n-1] = nums + [n-1]
#                 result(n-1, nums + [n-1])
#         else:
#             num[n - 1] = nums + [n - 1]
#             result(n - 1, nums + [n - 1])
#
# result(N, [N])
# print(len(num[1]) - 1)
# print(*num[1])