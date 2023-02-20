# https://www.acmicpc.net/problem/11660
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())

result = [0]

for _ in range(N):
    a, b, c, d = map(int, input().split())
    # if result:
    result.append(result[-1] + a)
    result.append(result[-1] + b)
    result.append(result[-1] + c)
    result.append(result[-1] + d)
    # else:
    #     result.append(a)
    #     result.append(result[-1] + b)
    #     result.append(result[-1] + c)
    #     result.append(result[-1] + d)
print(result)
for test_case in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    # print(result[(x2 - 1) * N + y2 ])
    # print(result[(x1 -1) * N + y1])
    print(result[(x2 - 1) * N + y2] - result[(x1 -1) * N + y1 - 1])