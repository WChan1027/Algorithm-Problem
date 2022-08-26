import sys

sys.stdin = open('input.txt')

T = int(input())        # 테스트 케이스 수

for test_case in range(1, T+1):
    N, M, K = map(int, input().split())     # N : 손님 수, M : 붕어빵 만드는 시간, K : 만들어지는 붕어빵 갯수

    booking_list = list(map(int, input().split()))      # 손님별 도착 시간

    for i in range(len(booking_list)-1):      # 시간 순 정렬
        for j in range(len(booking_list)-2, i-1, -1):
            if booking_list[j] > booking_list[j+1]:
                booking_list[j], booking_list[j+1] = booking_list[j+1], booking_list[j]

    time = -1
    bread = -K
    result = 'Possible'     # 일단 Possible
    while booking_list:
        time += 1
        if time % M == 0:       # 시간 M 이 지나면 K 만큼 붕어빵 증가
            bread += K
        while True:
            if booking_list[0] == time:     # 다음 손님이 도착하면
                bread -= 1      # 빵 1개 감소
                booking_list.pop(0)     # 빵 받은 손님 퇴장
                if not booking_list:        # 남은 손님이 없으면
                    break       # 장사 끝
            else:       # 다음 손님이 아직 안오면
                break       # 준비시간
        if bread < 0:       # 손님에게 줄 빵이 부족하면
            result = 'Impossible'       # Impossible
            break

    print(f'#{test_case} {result}')