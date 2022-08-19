T = int(input())

for test_case in range(1, T+1):
    N, Q = map(int, input().split())
    boxes = [0] * N

    for i in range(1, Q+1):
        L, R = map(int, input().split())
        for j in range(L-1, R):
            boxes[j] = i

    result = ''
    for i in range(len(boxes)):
        result += f'{boxes[i]} '

    print(f'#{test_case} {result}')