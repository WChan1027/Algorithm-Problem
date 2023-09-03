import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

T = int(input())

for test_case in range(T):
    N = int(input().strip())
    nums = list(map(int, input().strip().split()))

    plus = 0
    minus = 0

    before = 1
    sum_num = 0
    for num in nums:
        if num < 0:
            if before == 1:
                if sum_num + num > 0:
                    sum_num += num
                else:
                    before = -1
                    sum_num = num
            else:
                sum_num += num

        elif num > 0:
            plus += 1

            if before == 1:
                sum_num = num

            else:
                before = 1
                if sum_num + num > 0:
                    sum_num += num

                else:
                    minus += 1
                    sum_num = num

    if sum_num < 0:
        minus += 1

    if plus > minus:
        print('YES')
    else:
        print('NO')