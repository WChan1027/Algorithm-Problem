# https://www.acmicpc.net/problem/2475

nums = list(map(int, input().split()))
nums_square = 0

for i in nums:
    nums_square += i**2

verify_nums = nums_square % 10

print(verify_nums)