import sys
sys.stdin = open('sample_input.txt')

T = int(input())

# 마지막 정류장부터 역으로 계산
# n : 정류장 번호, num : 교체 횟수
def station(n, num):
    if n == 1:      # 출발지에 도달하면 num 반환
        return num
    for i in range(1, n):       # 출발지에 가까운 정류장부터 순회
        if i + battery[i] >= n:     # i 정류장에서 배터리를 갈았을 때 n 정류장까지 갈 수 있으면
            return station(i, num+1)        # i 정류장에서 배터리 교체

for test_case in range(1, T+1):
    battery = list(map(int, input().split()))
    N = battery[0]
    answer = station(N, 0) - 1      # 출발지 배터리 장착 횟수 -1

    print(f'#{test_case} {answer}')