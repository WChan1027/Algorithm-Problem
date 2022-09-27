import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for test_case in range(1, T+1):
    N = int(input())

    synergy = []
    for _ in range(N):
        synergy.append(list(map(int, input().split())))

    answer = 0
    for i in range(N):
        for j in range(N):
            answer += synergy[i][j]

    for i in range(1 << N):
        A = []
        B = []
        taste_A = 0
        taste_B = 0
        for j in range(N):
            if i & (1 << j):
                A.append(j)
        if len(A) == N//2:
            for j in range(N):
                if j not in A:
                    B.append(j)

            for j in A:
                for k in A:
                    taste_A += synergy[j][k]

            for j in B:
                for k in B:
                    taste_B += synergy[j][k]

            taste_diff = abs(taste_A - taste_B)

            if taste_diff < answer:
                answer = taste_diff

    print(f'#{test_case} {answer}')