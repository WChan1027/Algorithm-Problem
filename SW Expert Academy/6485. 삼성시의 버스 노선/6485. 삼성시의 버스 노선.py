T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    route = {}
    result = ''

    for i in range(N):
        A, B = map(int, input().split())
        for j in range(A, B+1):
            if j in route:
                route[j] += 1
            else:
                route[j] = 1

    P = int(input())
    station = [0]*5000
    for i in range(len(route.values())):
        station[list(route.keys())[i]-1] = list(route.values())[i]

    for i in range(1, P+1):
        J = int(input())
        result += f'{station[J-1]} '

    print(f'#{test_case} {result}')
