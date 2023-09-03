import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

T = int(input())

for test_case in range(T):
    N, M = map(int, input().split())

    time = 0

    while True:
        time += 1
        if (N-time) % N == time % M:
            break

        A2 = N - (time - (int(time/N) * N)) + 1
        B2 = time - int(time/M) * M + 1

    print(time)