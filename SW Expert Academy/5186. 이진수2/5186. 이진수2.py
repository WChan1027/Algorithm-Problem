import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for test_case in range(1, T+1):
    N = float(input())
    answer = ''
    count = 1
    n = 1
    while count < 13:
        count += 1
        n = n/2
        if N >= n:
            answer += '1'
            N = N - n
            if N == 0:
                break
        else:
            answer += '0'

    if N != 0:
        answer = 'overflow'

    print(f'#{test_case} {answer}')