import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for test_case in range(1, T+1):
    N = int(input())

    for i in range(1, N+1):
        if i**3 == N:
            answer = i
            break
        if i**3 > N:
            answer = -1
            break

    print(f'#{test_case} {answer}')