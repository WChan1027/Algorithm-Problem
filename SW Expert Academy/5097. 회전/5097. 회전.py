import sys

sys.stdin = open('sample_input.txt')

T = int(input())

for test_cases in range(1, T+1):
    N, M = map(int, input().split())
    sequence = list(map(int, input().split()))
    
    answer = sequence[M % N]

    print(f'#{test_cases} {answer}')