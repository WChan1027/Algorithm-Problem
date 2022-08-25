import sys

sys.stdin = open('sample_input.txt')

T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    C = list(map(int, input().split()))
    num = list(range(N))        # 피자 번호
    answer = 0
    turn = -1

    for i in range(M-1):        # 1개의 피자 빼고 치즈가 다 녹을 때까지 반복
        while True:
            turn += 1
            C[turn % N] = C[turn % N] // 2      # N개의 피자에 대해 치즈가 녹음
            if C[turn % N] == 0:        # turn % N 번째 피자의 치즈가 다 녹으면
                if i < M - N:       # 남은 피자가 있을 때
                    C[turn % N] = C[N + i]      # 치즈가 다 녹은 피자를 빼고 다음 피자를 넣음
                    num[turn % N] = N + i + 1       # 피자 번호에 새로 들어온 피자의 번호를 갱신
                else:       # 새로 들어올 피자가 없으면 빈 자리를 큰 수로 설정 (0이면 계산에 영향이 가서)
                    C[turn % N] = 100000000
                break       # 피자 1개의 치즈가 다 녹았으므로 다음 반복으로 넘어감

    for i in range(N):      # 피자 1개 빼고 치즈가 다 녹았으나 빈 자리를 큰 수로 설정했으므로 치즈가 남은 피자는 가장 작은 값으로 남아있음
        if C[i] < C[answer]:        # 치즈가 남은 피자의 화덕 내 위치를 구한 후 해당 위치의 피자 번호를 알아냄
            answer = i

    print(f'#{test_case} {num[answer]}')