import sys
sys.stdin = open('re_sample_input.txt')

T = int(input())

for test_case in range(1, T+1):
    N = int(input())

    island_x = list(map(int, input().split()))
    island_y = list(map(int, input().split()))
    E = float(input())

    length = [[0] * N for _ in range(N)]
    connect = [0] * N
    route = [[0] * N for _ in range(N)]
