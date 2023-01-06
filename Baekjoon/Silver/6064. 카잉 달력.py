    # https://www.acmicpc.net/problem/6064
    import sys
    sys.stdin = open('input.txt')
    input = sys.stdin.readline

    T = int(input())

    for test_case in range(1, T+1):
        M, N, x, y = map(int, input().split())

        year = 1
        now_x, now_y = 1, 1

        while now_x != x or now_y != y:
            if now_x == M and now_y == N:
                break
            now_x += 1
            now_y += 1
            if now_x > M:
                now_x = 1
            if now_y > N:
                now_y = 1
            year += 1

        if now_x == x and now_y == y:
            print(year)
        else:
            print(-1)