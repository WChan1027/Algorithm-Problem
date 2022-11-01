'''
https://www.acmicpc.net/problem/2293

[문제]

n가지 종류의 동전이 있다.
각각의 동전이 나타내는 가치는 다르다.
이 동전을 적당히 사용해서, 그 가치의 합이 k원이 되도록 하고 싶다.
그 경우의 수를 구하시오.
각각의 동전은 몇 개라도 사용할 수 있다.

사용한 동전의 구성이 같은데, 순서만 다른 것은 같은 경우이다.

'''
import sys
from collections import deque
from itertools import combinations_with_replacement

sys.stdin = open('input.txt')

n, k = map(int, sys.stdin.readline().split())

coin = [int(sys.stdin.readline().strip()) for _ in range(n)]


# # 1
# # DFS

# coin_answer = []
#
# stack = deque()
# stack.append([0]*n)
# while stack:
#     coin_count = stack.pop()
#     for i in range(len(coin)):
#         next_coin_count = [0]*n
#         for j in range(len(coin_count)):
#             next_coin_count[j] = coin_count[j]
#         next_coin_count[i] += 1
#         total = 0
#         for j in range(len(coin)):
#             total += next_coin_count[j] * coin[j]
#         if total == k:
#             if next_coin_count not in coin_answer:
#                 coin_answer.append(next_coin_count)
#         elif total < k:
#             stack.append(next_coin_count)
#
# print(len(coin_answer))



# # 2

# coin_count = [0]*n
# coin_answer = []
#
# def coin_fit(coin_count, k):
#     for i in range(len(coin)):
#         next_coin_count = [0]*n
#         for j in range(len(coin_count)):
#             next_coin_count[j] = coin_count[j]
#         next_coin_count[i] += 1
#         total = 0
#         for j in range(len(coin)):
#             total += coin_count[j] * coin[j]
#         if total == k:
#             if coin_count not in coin_answer:
#                 coin_answer.append(coin_count)
#             return
#         elif total < k:
#             coin_fit(next_coin_count, k)
#         else:
#             return
#
# coin_fit(coin_count, k)
# print(len(coin_answer))



# # 3

# answer = 0
# coin.sort(reverse=True)
# coin_count = []
# for i in coin:
#     for j in range(k//i):
#         coin_count.append(i)
#
# stack = deque()
# visited = 10001
# for i in coin:
#     stack.append(i)
#     while stack:
#         for i in coin_count:
#             if i < visited:
#                 if sum(stack) + i < k:
#                     stack.append(i)
#                 elif sum(stack) + i == k:
#                     stack.append(i)
#                     answer += 1
#                     break
#         visited = stack.pop()
#
# print(answer)



# # 4
#
# answer = 0
# for i in range(k//max(coin), k//min(coin) + 1):
#     for case in combinations_with_replacement(coin, i):
#         if sum(case) == k:
#             answer += 1
#
# print(answer)



# 5

coin_answer = []
def coin_count(n):
