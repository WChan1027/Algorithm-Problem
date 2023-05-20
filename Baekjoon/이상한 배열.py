import sys
from collections import defaultdict
sys.stdin = open('input.txt')
input = sys.stdin.readline

T = int(input())

for test_case in range(T):
    N = int(input())
    A = list(map(int, input().split()))

    check = defaultdict(lambda: True)

    for num in A:
        for key in check.keys():
            if key < num and check[key]:
                check[key] = False

        if not check[num]:
            print('No')
            break
    else:
        print('Yes')