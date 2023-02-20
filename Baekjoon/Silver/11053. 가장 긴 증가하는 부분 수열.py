# https://www.acmicpc.net/problem/11053
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
array = list(map(int, input().split()))

answer = 0


num = [1] * len(array)

for i in range(len(array)):
    for j in range(i, len(array)):
        if array[i] < array[j]:
            num[j] = max(num[i] + 1, num[j])

print(max(num))