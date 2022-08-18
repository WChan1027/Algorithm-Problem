T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    a = list(map(int, input().split()))

    max = 0
    min = N*10000

    for i in range(0, N-M+1):
        sum = 0
        for j in range(M):
            sum += a[i+j]
        if sum > max:
            max = sum
        
        if sum < min:
            min = sum
    
    print(f'#{test_case} {max - min}')