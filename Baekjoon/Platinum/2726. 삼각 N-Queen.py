# https://www.acmicpc.net/problem/2726
import sys
# sys.setrecursionlimit(10**5)
sys.stdin = open('input.txt')
input = sys.stdin.readline

C = int(input())


for test_case in range(C):
    N = int(input())

    answer = (2*N +1)//3
    board = [(0, 0)] * answer

    if N % 3 == 0:
        for i in range(1, 1 + answer//2):
            board[i] = (N//3 + i, 2*i - 1)

        for i in range(1, answer//2):
            board[answer//2 + i] = (answer//2 + N//3 + i, 2*i)

    elif N % 3 == 1:
        for i in range(answer//2 + 1):
            board[i] = (N//3 + i, 2*i)

        for i in range(1, answer//2 + 1):
            board[answer//2 + i] = (answer//2 + N//3 + i, 2*i -1)

    else:
        if N > 2:
            board[1] = (2, 1)
        for i in range(2, answer//2 +2):
            board[i] = (N//3 + i + 1, 2*(i-1))

        for i in range(2, answer//2 + 1):
            board[answer//2 + i] = (answer//2 + N//3 + i + 1, 2*i -1)





# def queen(row, queens, N, num):
#     global answer, board, flag
#     if flag == 1:
#         return
#
#     if row == N-1:
#         for i in range(row+1):
#             if check(queens, (row, i)) == 1:
#                 num += 1
#                 queens += [(row, i)]
#
#                 if num == answer:
#                     board = queens
#                     flag = 1
#                 return
#
#         if num == answer:
#             board = queens
#             flag = 1
#         return
#
#     for i in range(row+1):
#         if check(queens, (row, i)) == 1:
#             queen(row + 1, queens + [(row, i)], N, num + 1)
#
#     queen(row + 1, queens, N, num)
#
#
#
# def check(arr, new):
#     new_x, new_y = new
#     for i in arr:
#         x, y = i
#         if y == new_y or new_x - x == new_y - y:
#             return 0
#
#     return 1

# for test_case in range(C):
    # board = []
    # flag = 0
    #
    # if N % 3 == 1:
    #     queen(N//3 + 1, [(N//3, 0)], N, 1)
    # elif N % 3 == 2:
    #     # if N > 5:
    #     #     queen(N//3 + 4, [(0, 0), (2, 1), (N//3 +3, 2)], N, 2)
    #     # else:
    #     #     queen(3, [(0, 0), (2, 1)], N, 2)
    #     queen(3, [(0, 0), (2, 1)], N, 2)
    #
    # else:
    #     queen(N//3 + 1, [(0, 0), (N//3 +1, 1)], N, 2)

    print(answer)
    for chess in board:
        print(chess[0] +1, chess[1] + 1)
    # print('N :', N, '/', answer, len(board), board)