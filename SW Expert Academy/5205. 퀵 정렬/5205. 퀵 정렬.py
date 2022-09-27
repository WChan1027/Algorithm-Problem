import sys
sys.stdin = open('sample_input.txt')

T = int(input())

def quick_sort(A, l, r):
    if l < r:
        s = partition(A, l, r)
        quick_sort(A, l, s-1)
        quick_sort(A, s+1, r)

def partition(A, l, r):
    p = A[l]
    i = l+1
    j = r
    while i <= j:
        while i <= j and A[i] <= p:
            i += 1
        while i <= j and A[j] >= p:
            j -= 1

        if i <= j:
            A[i], A[j] = A[j], A[i]
    A[l], A[j] = A[j], A[l]

    return j


for test_case in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))

    quick_sort(nums, 0, N-1)

    print(f'#{test_case} {nums[N//2]}')