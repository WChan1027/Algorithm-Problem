# https://www.acmicpc.net/problem/9019

import sys
from collections import deque

sys.stadin = open('input.txt')

T = int(sys.stadin.readline())

for test_case in range(T):
    A, B = map(int, sys.stadin.readline().strip().split())

    stack = deque()
    stack.append((A, ''))
    visited = [0] * 10000

    while stack:
        num, answer = stack.popleft()

        if num == B:
            print(answer)
            break

        visited[num] = 1

        # next_num = [(num*2) % 10000, (num-1) % 10000, (num*10 + num//1000) % 10000, (num//10 + (num%10)*1000) % 10000]
        # next_regi = ['D', 'S', 'L', 'R']
        #
        # for i in range(4):
        #     if visited[next_num[i]] == 0:
        #         stack.append([next_num[i], answer + next_regi[i]])
        #         visited[next_num[i]] = 1

        nextD = (num*2) % 10000
        nextS = (num-1) % 10000
        nextL = (num*10 + num//1000) % 10000
        nextR = (num//10 + (num%10)*1000) % 10000

        if visited[nextD] == 0:
            stack.append((nextD, answer + 'D'))
            visited[nextD] = 1

        if visited[nextS] == 0:
            stack.append((nextS, answer + 'S'))
            visited[nextS] = 1

        if visited[nextL] == 0:
            stack.append((nextL, answer + 'L'))
            visited[nextL] = 1

        if visited[nextR] == 0:
            stack.append((nextR, answer + 'R'))
            visited[nextR] = 1