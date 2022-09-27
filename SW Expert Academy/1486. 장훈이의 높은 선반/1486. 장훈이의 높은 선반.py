import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    N, B = map(int, input().split())

    height = list(map(int, input().split()))
    result = sum(height)

    for i in range(1 << N):
        tmp = []
        for j in range(N):
            if i & (1 << j):
                tmp.append(height[j])
        if B <= sum(tmp) < result:
            result = sum(tmp)

    answer = result - B

    print(f'#{test_case} {answer}')