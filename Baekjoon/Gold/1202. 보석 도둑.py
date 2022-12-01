# https://www.acmicpc.net/problem/1202
import sys
sys.stdin = open('input.txt')

# N, K = map(int, sys.stdin.readline().split())
#
# jewel = [0] * N
# bag = [0] * K
# get_jewel = [0] * N
# get_bag = [0] * K
# count = 0
#
# for i in range(N):
#     M, V = map(int, sys.stdin.readline().split())
#     jewel[i] = (M, V, i)
#
# for i in range(K):
#     C = int(sys.stdin.readline())
#     bag[i] = C
#
# sorted(jewel, key=lambda jewel : jewel[0], reverse=True)
# sorted(bag)
#
# for i in range(N):
#     for j in range(K):
#         if get_bag[j] == 0 and jewel[i][0] <= bag[j]:
#             get_bag[j] = (jewel[i][1], j, jewel[i][2])
#             get_jewel[jewel[i][2]] = 1
#             count += 1
#             break
#
#     if count == K:
#         break
#
# sorted(jewel, key=lambda jewel : jewel[1], reverse=True)
# sorted(get_bag, key=lambda get_bag : get_bag[0])
#
# for i in range(N):
#     if get_jewel[jewel[i][2]] == 0:
#         for j in range(K):
#             if jewel[i][1] > get_bag[j][0] and bag[get_bag[j][1]] >= jewel[i][0]:
#                 get_jewel[jewel[i][2]] = 1
#                 get_jewel[get_bag[j][2]] = 0
#                 get_bag[j] = (jewel[i][1], get_bag[j][1], jewel[i][2])
#                 break
#
# answer = 0
# for i in get_bag:
#     answer += i[0]
#
# print(answer)



# N, K = map(int, sys.stdin.readline().split())
#
# jewel = [0] * N
# bag = [0] * K
# bag_full = [0] * K
# get = [0] * K
#
# for i in range(N):
#     M, V = map(int, sys.stdin.readline().split())
#     jewel[i] = (M, V)
#
# for i in range(K):
#     C = int(sys.stdin.readline())
#     bag[i] = C
#
# sorted(jewel, key=lambda jewel : jewel[1], reverse=True)
# sorted(bag)
#
# for i in range(N):
#     for j in range(K):
#         if bag_full[j] == 0 and jewel[i][0] < bag[j]:
#             get[j] = jewel[i][1]
#             bag_full[j] = 1
#             break
#
# print(sum(get))



# from collections import deque
# N, K = map(int, sys.stdin.readline().split())
#
# jewels = deque()
# bag = [0] * K
# bag_full = [0] * K
# get = [0] * K
#
# for i in range(N):
#     M, V = map(int, sys.stdin.readline().split())
#     jewels.append((M, V))
#
# for i in range(K):
#     C = int(sys.stdin.readline())
#     bag[i] = C
#
# for i in range(len(jewels)):
#     for j in range(len(jewels)-1, i, -1):
#         if jewels[j][1] < jewels[j-1][1]:
#             jewels[j], jewels[j-1] = jewels[j-1], jewels[j]
#
# sorted(bag)
#
# while jewels:
#     jewel = jewels.pop()
#     for j in range(K):
#         if bag_full[j] == 0 and jewel[0] < bag[j]:
#             get[j] = jewel[1]
#             bag_full[j] = 1
#             break
#
# print(sum(get))



import heapq
N, K = map(int, sys.stdin.readline().split())

jewels = []
bags = []
get = []
answer = 0

for i in range(N):
    M, V = map(int, sys.stdin.readline().split())
    heapq.heappush(jewels, (M, V))

for i in range(K):
    C = int(sys.stdin.readline())
    heapq.heappush(bags, C)

while bags:
    bag = heapq.heappop(bags)
    while jewels and jewels[0][0] <= bag:
        heapq.heappush(get, -heapq.heappop(jewels)[1])
    if get:
        answer += -heapq.heappop(get)

print(answer)