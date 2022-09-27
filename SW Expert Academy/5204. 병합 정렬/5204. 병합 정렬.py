import sys
sys.stdin = open('sample_input.txt')

T = int(input())

def merge_sort(arr):
    if len(arr) == 1:
        return  arr

    middle = len(arr) // 2
    left = arr[:middle]
    right = arr[middle:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def merge(left, right):
    global answer
    if left[len(left)-1] > right[len(right)-1]:
        answer += 1

    result = []

    l_idx = r_idx = 0
    while l_idx < len(left) and r_idx < len(right):
        if left[l_idx] <= right[r_idx]:
            result.append(left[l_idx])
            l_idx += 1
        else:
            result.append(right[r_idx])
            r_idx += 1

    if l_idx < len(left):
        result += left[l_idx:]
    else:
        result += right[r_idx:]

    return result


for test_case in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))

    answer = 0
    answer_list = merge_sort(nums)

    print(f'#{test_case} {answer_list[N//2]} {answer}')