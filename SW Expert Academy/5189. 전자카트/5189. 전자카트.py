import sys
sys.stdin = open('sample_input.txt')

T = int(input())

# 해당 경로가 최솟값인지 확인하는 함수
def min_energy(route):
    global answer
    result = 0
    for i in range(len(route) - 1):
        result += battery[route[i]][route[i+1]]
        if result > answer:
            return

    if result < answer:
        answer = result
        return

# 가능한 경로를 구하는 함수
def go(a, N):
    if a == N:
        route.append(0)
        min_energy(route)
        route.pop()
        return

    for i in range(N):
        if went[i] == 0:
            route.append(sector[i])
            went[i] = 1
            go(a+1, N)
            route.pop()
            went[i] = 0

for test_case in range(1, T+1):
    N = int(input())

    battery = []
    for _ in range(N):
        battery.append(list(map(int, input().split())))

    sector = [i for i in range(N)]
    route = [0]
    went = [0] * N
    answer = 100 * N

    went[0] = 1

    go(1, N)

    print(f'#{test_case} {answer}')