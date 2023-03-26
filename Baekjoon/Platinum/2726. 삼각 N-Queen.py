# https://www.acmicpc.net/problem/2726
import sys
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

    print(answer)
    for chess in board:
        print(chess[0] +1, chess[1] + 1)