'''
https://www.acmicpc.net/problem/10818

[문제]

N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.

'''

N = int(input())
nums = list(map(int, input().split()))

max = nums[0]
min = nums[0]

for i in nums:
    if i > max:
        max = i
    elif i < min:
        min = i

print(min, max)