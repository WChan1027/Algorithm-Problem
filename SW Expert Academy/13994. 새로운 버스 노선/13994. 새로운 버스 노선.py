import sys

sys.stdin = open('sample_in.txt')

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    station = [0] * 1001

    for i in range(N):
        bus = list(map(int, input().split()))

        if bus[0] == 1:     # 일반 버스일 때
            for j in range(bus[1], bus[2]+1):   # 출발 정류장부터 도착 정류장까지 +1
                station[j] += 1

        elif bus[0] == 2:       # 급행 버스일 때
            for j in range(bus[1], bus[2]):      # 출발 정류장부터 도착 정류장 전까지 2정류장마다 +1
                if j % 2 == bus[1] % 2:
                    station[j] += 1
            station[bus[2]] += 1        # 도착 정류장 +1

        elif bus[0] == 3:       # 광역 급행 버스일 때
            if bus[1] % 2 == 0:     # 짝수 정류장부터 출발할 때
                for j in range(bus[1] + 1, bus[2]):       # 출발 정류장 다음 정류장부터 도착 정류장 전까지 4의 배수 정류장마다 +1
                    if j % 4 == 0:
                        station[j] += 1
                station[bus[1]] += 1        # 출발 정류장 +1
                station[bus[2]] += 1        # 도착 정류장 +1
            else:       # 홀수 정류장부터 출발할 때
                for j in range(bus[1] + 1, bus[2]):       # 출발 정류장 다음 정류장부터 도착 정류장 전까지 3의 배수이면서 10의 배수가 아닌 정류장마다 +1
                    if j % 3 == 0 and j % 10 != 0:
                        station[j] += 1
                station[bus[1]] += 1        # 출발 정류장 +1
                station[bus[2]] += 1        # 도착 정류장 +1

    answer = max(station)
    print(f'#{test_case} {answer}')