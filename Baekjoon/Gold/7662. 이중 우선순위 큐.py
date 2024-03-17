# https://www.acmicpc.net/problem/7662

import sys
import heapq
sys.stdin = open('input.txt')

T = int(sys.stdin.readline().strip())

for test_case in range(T):
    k = int(sys.stdin.readline().strip())
    min_num = []
    max_num = []
    visited = [0] * 1000001

    for i in range(k):
        word, n = map(str, sys.stdin.readline().strip().split())
        n = int(n)

        if word == 'I':
            heapq.heappush(min_num, (n, i))
            heapq.heappush(max_num, (-n, i))
            visited[i] = 1
        else:
            if n == 1:
                while max_num and visited[max_num[0][1]] == 0:
                    heapq.heappop(max_num)
                if max_num:
                    visited[max_num[0][1]] = 0
                    heapq.heappop(max_num)
            else:
                while min_num and visited[min_num[0][1]] == 0:
                    heapq.heappop(min_num)
                if min_num:
                    visited[min_num[0][1]] = 0
                    heapq.heappop(min_num)

    while min_num and visited[min_num[0][1]] == 0:
        heapq.heappop(min_num)
    while max_num and visited[max_num[0][1]] == 0:
        heapq.heappop(max_num)

    if len(max_num) == 0:
        print('EMPTY')
    else:
        print(-max_num[0][0], min_num[0][0])
