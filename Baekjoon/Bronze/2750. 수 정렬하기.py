'''
https://www.acmicpc.net/problem/2750

[문제]

N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

'''

def merge_sort(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort(arr[mid:])

    merged_arr = []
    a = 0
    b = 0
    while a < len(low_arr) and b < len(high_arr):
        if low_arr[a] < high_arr[b]:
            merged_arr.append(low_arr[a])
            a += 1
        else:
            merged_arr.append(high_arr[b])
            b += 1

    merged_arr += low_arr[a:]
    merged_arr += high_arr[b:]
    return merged_arr

N = int(input())
result = []

for _ in range(N):
    result.append(int(input()))

for i in merge_sort(result):
    print(i)