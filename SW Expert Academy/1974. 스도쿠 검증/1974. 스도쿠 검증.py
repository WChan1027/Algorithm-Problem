import sys

sys.stdin = open('input.txt')

def verified(nums):
    verified = {}
    for _ in range(1, 10):
        verified[_] = 0

    for i in nums:
        verified[i] += 1

    if 0 in verified.values():
        return 0

    return 1

T = int(input())

for test_case in range(1, T+1):

    sudoku = []
    nums = []
    result = 1

    for length in range(9):
        sudoku += [list(map(int, input().split()))]

    for i in range(9):
        for j in range(9):
            nums += [sudoku[i][j]]
        result *= verified(nums)
        nums = []

        for j in range(9):
            nums += [sudoku[j][i]]
        result *= verified(nums)
        nums = []
        if result == 0:
            break

    if result == 1:
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                for k in range(3):
                    for l in range(3):
                        nums += [sudoku[i+k][j+l]]
                result *= verified(nums)
                nums = []
                if result == 0:
                    break
            if result == 0:
                break

    print(f'#{test_case} {result}')