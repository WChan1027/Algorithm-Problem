# https://www.acmicpc.net/problem/9663
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())

answer = 0

column = [0] * N

def queen(row, n, queens):
    global answer
    if n == N:
        for i in range(N):
            if column[i] == 0 and check(queens, (row, i)) == 1:
                answer += 1
        return

    for i in range(N):
        if column[i] == 0 and check(queens, (row, i)) == 1:
            column[i] = 1
            queen(row + 1, n+1, queens + [(row, i)])
            column[i] = 0

def check(arr, new):
    new_x, new_y = new
    for i in arr:
        x, y = i
        if x == new_x or abs(new_x - x) == abs(new_y - y):
            return 0

    return 1

queen(0, 1, [])

print(answer)




# rows = [0] * N
#
# def queen(n):
#     global answer
#     if n == N-1:
#         for i in range(N):
#             if check(n, i) == 1:
#                 answer += 1
#         return
#
#     for i in range(N):
#         if check(n, i) == 1:
#             rows[n] = i
#             queen(n+1)
#             rows[n] = 0
#
# def check(row, column):
#     for line in range(row):
#         if rows[line] == column or abs(line - row) == abs(rows[line] - column):
#             return 0
#     return 1
#
# queen(0)
# print(answer)


# row_column_sum = [0] * N
#
# def queen(n):
#     global answer
#     if n == N-1:
#         for i in range(N):
#             if check(n, i) == 1:
#                 answer += 1
#         return
#
#     for i in range(N):
#         if check(n, i) == 1:
#             row_column_sum[n] = n+i
#             queen(n+1)
#             row_column_sum[n] = 0
#
# def check(row, column):
#     a = row + column
#     for line in range(row):
#         if a == row_column_sum[line] or a == row_column_sum[line] + row - line or a == row_column_sum[line] + 2 * (row - line):
#             return 0
#     return 1
#
# queen(0)
# print(answer)




# def queen(line, n, queens):
#     global answer
#     if n == N:
#         for i in range(N):
#             if check(queens, (line, i)) == 1:
#                 answer += 1
#         return
#     for i in range(N):
#         if check(queens, (line, i)) == 1:
#             queen(line + 1, n+1, queens + [(line, i)])
#
#
# def check(arr, new):
#     new_x, new_y = new
#     for i in arr:
#         x, y = i
#         if x == new_x or y == new_y or abs(new_x - x) == abs(new_y - y):
#             return 0
#
#     return 1
#
# queen(0, 1, [])
#
# print(answer)