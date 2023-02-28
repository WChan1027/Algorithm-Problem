# https://www.acmicpc.net/contest/problem/956/4
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

Q = int(input())

sum = 0

def calc(a, b):
    if 2*a > b and a <= b:
        return a

    result = a * a
    if result < b:
        return calc(result, b)
    elif result == b:
        return result
    else:
        c = calc(2, b // a)
        return a * c


for test_case in range(Q):
    query = input().strip()
    num = int(query[1:])

    if query[0] == '+':
        sum += num

        if sum == 0:
            print(0)
        elif sum == 1:
            print(1)
        else:
            print(calc(2, sum))


    else:
        sum -= num

        if sum == 0:
            print(0)
        elif sum == 1:
            print(1)
        else:
            print(calc(2, sum))