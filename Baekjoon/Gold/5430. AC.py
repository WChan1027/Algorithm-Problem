import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

T = int(sys.stdin.readline().strip())

for test_case in range(T):
    p = input().strip()
    n = int(input().strip())
    nums = input().rstrip()[1:-1].split(',')
    answer = '[]'

    if n:
        nums = list(map(int, nums))

        i, j = 0, n
        is_forward = True

        if p.count('D') > n:
            answer = 'error'
        elif p.count('D') < n:
            for task in p:
                if task == 'R':
                    is_forward = not is_forward
                else:
                    if is_forward:
                        i += 1
                    else:
                        j -= 1

            if is_forward:
                answer = str(nums[i:j])
            else:
                answer = str(nums[i:j][::-1])

    else:
        if 'D' in p:
            answer = 'error'

    answer = answer.replace(' ', '')
    print(answer)