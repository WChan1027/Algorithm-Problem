import sys

sys.stdin = open('sample_input.txt')

T = int(input())

# N일 때 값을 구하는 함수
def cases(N):
    if N > 2 and len(case) <= N:
        case.append(2*cases(N-2) + cases(N-1))
    return case[N]


for test_case in range(1, T+1):
    N = int(input())
    N = N//10
    case = [0, 1, 3]    # N = 0, 1, 2 일때의 값
    answer = cases(N)

    print(f'#{test_case} {answer}')