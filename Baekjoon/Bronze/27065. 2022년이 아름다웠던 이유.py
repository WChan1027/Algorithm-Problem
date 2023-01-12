# https://www.acmicpc.net/problem/27065
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

T = int(input())

def divisor(N):
    num = [1]
    for i in range(2, N//2+1):
        if N % i == 0:
            num.append(i)

    return num

def check(N):
    if N >= sum(divisor(N)):
        return 0
    else:
        return 1

for test_case in range(T):
    n = int(input())
    div = divisor(n)
    no = 0
    if check(n) == 1:
        for num in div:
            if check(num) != 0:
                no = 1
                print('BOJ 2022')
                break

        if no == 0:
            print('Good Bye')

    else:
        print('BOJ 2022')