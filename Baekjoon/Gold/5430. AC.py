# https://www.acmicpc.net/problem/5430

import sys
from collections import deque
sys.stdin = open('input.txt')

T = int(sys.stdin.readline().strip())

for _ in range(T):
    p = sys.stdin.readline().strip()
    n = int(sys.stdin.readline().strip())

    num = sys.stdin.readline().rstrip()[1:-1].split(',')
    num_list = deque(num)

    flag = 0
    end = 0
    for i in p:
        if i == 'R':
            flag += 1
        else:
            if not num_list or n == 0:
                print('error')
                end = 1
                break
            if flag % 2 == 0:
                num_list.popleft()
            else:
                num_list.pop()
    if end == 0:
        a = 0
        if flag % 2 == 1:
            num_list.reverse()
        answer = '['
        for i in num_list:
            answer += str(i)
            answer += ','
            a = 1
        if a == 1:
            answer = answer[:-1]
        answer += ']'

        print(answer)