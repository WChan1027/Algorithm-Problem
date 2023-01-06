# https://www.acmicpc.net/problem/17626
import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())

# end = 0
# que = deque()
# for i in range(1, 225):
#     if i**2 == n:
#         print(1)
#         end = 1
#         break
#     elif i**2 < n:
#         que.append((n - i**2, 1))
#     else:
#         break
#
# while que and end == 0:
#     num, cnt = que.popleft()
#     if cnt == 4:
#         pass
#     else:
#         for i in range(1, 225):
#             if i**2 == num:
#                 print(cnt + 1)
#                 end = 1
#                 break
#             elif i**2 < num:
#                 que.append((num - i**2, cnt + 1))
#             else:
#                 break

lagrangian = [0] * 50001

for i in range(1, 224):
    lagrangian[i**2] = 1

cnt = 0
while lagrangian[n] == 0:
    cnt += 1
    for i in range(1, n):
        if lagrangian[i] == cnt:
            for j in range(1, 224):
                if i + j**2 <= n:
                    if lagrangian[i + j**2] == 0:
                        lagrangian[i + j**2] = cnt + 1
                else:
                    break
        if lagrangian[n] != 0:
            break

print(lagrangian[n])