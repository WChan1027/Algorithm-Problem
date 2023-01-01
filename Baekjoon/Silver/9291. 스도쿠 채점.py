# https://www.acmicpc.net/problem/9291
import sys
sys.stdin = open('input.txt')

T = int(sys.stdin.readline())

def check(arr):
    if sum(arr) == 45:
        multiple = 1
        for i in arr:
            multiple *= i
        if multiple == 362880:
            return 1
    return 0

for test_case in range(1, T+1):
    if 1 < test_case <= T:
        space = sys.stdin.readline()
    sudoku = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]
    result = 1
    for i in range(9):
        if check(sudoku[i]) == 0:
            result = 0
            break

    if result == 1:
        for i in range(9):
            arr = []
            for j in range(9):
                arr.append(sudoku[j][i])
            if check(arr) == 0:
                result = 0
                break

    if result == 1:
        for x in [0, 3, 6]:
            for y in [0, 3, 6]:
                arr = []
                for i in range(3):
                    for j in range(3):
                        arr.append(sudoku[x+i][y+j])
                if check(arr) == 0:
                    result = 0
                    break

    if result == 1:
        print(f'Case {test_case}: CORRECT')
    else:
        print(f'Case {test_case}: INCORRECT')
