import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    weight = list(map(int, input().split()))
    capacity = list(map(int, input().split()))

    weight.sort(reverse=True)
    capacity.sort()
    used_container = [0] * N
    used_truck = [0] * M
    answer = 0

    for i in range(N):
        for j in range(M):
            if used_container[i] == 0 and used_truck[j] == 0:
                if weight[i] <= capacity[j]:
                    used_container[i] = 1
                    used_truck[j] = 1
                    answer += weight[i]
                    break

    print(f'#{test_case} {answer}')