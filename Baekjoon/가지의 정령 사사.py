import sys
from pprint import pprint
sys.stdin = open('input.txt')
input = sys.stdin.readline

T = int(input())

for test_case in range(T):
    n = int(input())

    answer = []
    field = list([0] * n for _ in range(n))
    for i in range(1, n+1):
        for j in range(1, n+1):
            s = i + j
            a = (i-1) * n + j
            if s > n+1:
                field[i-1][j-1] = n*n - sum(k for k in range(1, 2*n - s + 1)) - (n-j)
                if n*n - sum(k for k in range(1, 2*n - s + 1)) - (n-j) == a:
                    answer.append(a)
            else:
                field[i-1][j-1] = sum(k for k in range(1, s-1)) + j
                if sum(k for k in range(1, s-1)) + j == a:
                    answer.append(a)
    pprint(field)
    print(*answer)