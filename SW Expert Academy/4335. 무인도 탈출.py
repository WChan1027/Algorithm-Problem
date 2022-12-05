# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWL6HGz6Ai4DFAUY&
import sys
sys.stdin = open('input.txt')

T = int(sys.stdin.readline())
# case = [(1, 1, 0), (1, 0, 1), (0, 1, 1)]
#
# def getHeight(width, length, height, visited):
#     global N, max_height
#     # high = height
#     # for i in range(N):
#     #     if visited[i] == 0:
#     #         high += max(boxes[i])
#     #
#     # if high <= max_height:
#     #     return
#
#
#     for i in range(N):
#         if visited[i] == 0:
#             small = 0
#             for j in range(3):
#                 if boxes[i][j] <= width:
#                     next_width = boxes[i][j]
#                     for k in range(3):
#                         if k != j and boxes[i][k] <= length:
#                             next_length = boxes[i][k]
#                             small = 1
#                             for l in range(3):
#                                 if l != j and l != k:
#                                     next_height = boxes[i][l]
#
#                             visited[i] = 1
#                             getHeight(next_width, next_length, height + next_height, visited)
#                             visited[i] = 0
#
#             # if small == 0:
#             #     visited[i] = 1
#
#     if height > max_height:
#         max_height = height
#
#     return
#
# # def getHeight(width, length, high):
# #     global N, max_height
# #     height = high
# #     for i in range(N):
# #         if visited[i] == 0:
# #             height += max(boxes[i])
# #
# #     if height <= max_height:
# #         return
# #
# #     for i in range(N):
# #         if visited[i] == 0:
# #             next_width, next_length, height = boxes[i][0], boxes[i][1], boxes[i][2]
# #             if next_width <= width and next_length <= length:
# #                 visited[i] = 1
# #                 getHeight(next_width, next_length, high + height)
# #                 visited[i] = 0
# #             elif next_width <= length and next_length <= width:
# #                 visited[i] = 1
# #                 getHeight(next_width, next_length, high + height)
# #                 visited[i] = 0
# #
# #
# #             next_width, next_length, height = boxes[i][0], boxes[i][2], boxes[i][1]
# #             if next_width <= width and next_length <= length:
# #                 visited[i] = 1
# #                 getHeight(next_width, next_length, high + height)
# #                 visited[i] = 0
# #             elif next_width <= length and next_length <= width:
# #                 visited[i] = 1
# #                 getHeight(next_width, next_length, high + height)
# #                 visited[i] = 0
# #
# #
# #             next_width, next_length, height = boxes[i][2], boxes[i][1], boxes[i][0]
# #             if next_width <= width and next_length <= length:
# #                 visited[i] = 1
# #                 getHeight(next_width, next_length, high + height)
# #                 visited[i] = 0
# #             elif next_width <= length and next_length <= width:
# #                 visited[i] = 1
# #                 getHeight(next_width, next_length, high + height)
# #                 visited[i] = 0
# #
# #             # for j in range(3):
# #             #     plane = []
# #             #     for k in range(3):
# #             #         if case[j][k] == 1:
# #             #             plane.append(boxes[i][k])
# #             #         else:
# #             #             height = boxes[i][k]
# #             #
# #             #     next_width, next_length = plane[0], plane[1]
# #             #
# #             #     if next_width <= width and next_length <= length:
# #             #         visited[i] = 1
# #             #         getHeight(next_width, next_length, high + height)
# #             #         visited[i] = 0
# #             #     elif next_width <= length and next_length <= width:
# #             #         visited[i] = 1
# #             #         getHeight(next_width, next_length, high + height)
# #             #         visited[i] = 0
# #
# #     if high > max_height:
# #         max_height = high
# #
# #     return
#
#
# for test_case in range(1, T+1):
#     N = int(sys.stdin.readline())
#     boxes = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
#
#     max_height = 0
#
#     # for i in range(N):
#     #     visited = [0] * N
#     #     visited[i] = 1
#     #
#     #     width, length, height = boxes[i][0], boxes[i][1], boxes[i][2]
#     #     getHeight(width, length, height)
#     #
#     #     width, length, height = boxes[i][0], boxes[i][2], boxes[i][1]
#     #     getHeight(width, length, height)
#     #
#     #     width, length, height = boxes[i][2], boxes[i][1], boxes[i][0]
#     #     getHeight(width, length, height)
#     #
#     #     visited[i] = 0
#
#
#     for i in range(N):
#         visited_start = [0] * N
#         visited_start[i] = 1
#         getHeight(boxes[i][0], boxes[i][1], boxes[i][2], visited_start)
#         getHeight(boxes[i][0], boxes[i][2], boxes[i][1], visited_start)
#         getHeight(boxes[i][2], boxes[i][1], boxes[i][0], visited_start)

for test_case in range(1, T+1):
    N = int(sys.stdin.readline())
    boxes = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    size = [[0]*3 for _ in range(N)]
    for i in range(N):
        for j in range(3):
            size[i][j] =

    print(size)

    # print(f'#{test_case}', max_height)