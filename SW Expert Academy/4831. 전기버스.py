T = int(input())

for test_case in range(1, T + 1):
    K, N, M = map(int,input().split())
    charge = list(map(int, input().split()))
    location = 0
    n = 0
    error = 0

    for i in range(M-1):
        if charge[i+1] - charge[i] > K:
            error = 1
            break
    
    if charge[0] > K:
        error = 1

    if N - charge[-1] > K:
        error = 1

    stop = 0
    if error == 0:
        while stop == 0:
            for i in range(M-1, -1, -1):
                if location + K >= N :
                    stop = 1

                else:
                    if location < charge[i] and location + K >= charge[i]:
                        location = charge[i]
                        n += 1

    print(f'#{test_case} {n}')