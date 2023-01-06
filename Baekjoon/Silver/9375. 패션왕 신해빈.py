# https://www.acmicpc.net/problem/9375
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

T = int(input())

for test_case in range(T):
    n = int(input())

    closet = dict()
    for _ in range(n):
        name, category = map(str, input().split())
        if category in closet.keys():
            closet[category] += 1
        else:
            closet[category] = 2

    answer = 1
    for i in closet.values():
        answer *= i

    print(answer - 1)