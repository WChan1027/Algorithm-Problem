# https://www.acmicpc.net/problem/12852
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())

num = [[0] * (N+1) for _ in range(N+1)]

def result(n, nums):
    if n == 1:
        if len(nums) < len(num[1]):
            num[1] = nums
        return

    if n % 3 == 0:
        n = n//3
        if len(num[n]) > len(nums) + 1:
            num[n] = nums + [n]
            result(n, nums + [n])

    if n % 2 == 0:
        n = n//2
        if len(num[n]) > len(nums) + 1:
            num[n] = nums + [n]
            result(n, nums + [n])

    if n > 1:
        if len(num[n-1]) > len(nums) + 1:
            num[n-1] = nums + [n-1]
            result(n-1, nums + [n-1])

result(N, [N])
print(num)
print(len(num[1]) - 1)
print(*num[1])