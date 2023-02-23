# https://www.acmicpc.net/problem/23291
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, K = map(int, input().split())
fishes = list(map(int, input().split()))

result = 1000000
turn = 0
n = int(N ** (1 / 2))
direction = [(0, -1), (1, 0), (0, 1), (-1, 0)]

while result > K:
    if turn > 0:
        fishes = sorted_fishes
    min_fish = min(fishes)
    for i in range(N):
        if fishes[i] == min_fish:
            fishes[i] += 1

    new_bowl = [[0] * (3*n +2) for _ in range(3*n + 2)]
    if N - n*n >= n:
        count = 2*n -1
        dir = count % 4
        now_x, now_y = n, n
        cnt = 0
        l = 1
        for i in range(n*n + n):
            cnt += 1
            new_bowl[now_x][now_y] = fishes[i]
            now_x += direction[dir][0]
            now_y += direction[dir][1]
            if cnt == int(l//1):
                cnt = 0
                l += 1/2
                dir = (dir + 1) % 4

        for i in range(n*n + n, N):
            new_bowl[now_x][now_y] = fishes[i]
            now_y += 1

    else:
        count = 2*n - 2
        dir = count % 4 -2
        now_x, now_y = n, n

        cnt = 0
        l = 1
        for i in range(n*n):
            cnt += 1
            new_bowl[now_x][now_y] = fishes[i]
            now_x += direction[dir][0]
            now_y += direction[dir][1]
            if cnt == int(l//1):
                cnt = 0
                l += 1/2
                dir = (dir + 1) % 4

        for i in range(n*n, N):
            new_bowl[now_x][now_y] = fishes[i]
            now_y += 1

    new_bowl2 = [[0] * (3*n +2) for _ in range(3*n +2)]

    for i in range(3*n +2):
        for j in range(3*n +2):
            new_bowl2[i][j] = new_bowl[i][j]

    for i in range(3*n +2):
        for j in range(3*n +2):
            if new_bowl[i][j] != 0:
                now_x, now_y = i, j
                for dir in direction:
                    next_x = now_x + dir[0]
                    next_y = now_y + dir[1]
                    if 0 <= next_x < 3*n + 2 and 0 <= next_y < 3*n + 2:
                        if new_bowl[next_x][next_y] != 0 and new_bowl[now_x][now_y] > new_bowl[next_x][next_y]:
                            d = (new_bowl[now_x][now_y] - new_bowl[next_x][next_y]) // 5
                            new_bowl2[now_x][now_y] -= d
                            new_bowl2[next_x][next_y] += d


    new_fish = [0] * N

    cnt = 0
    flag = 0
    for i in range(3*n +1, -1, -1):
        for j in range(3*n +2):
            if new_bowl2[i][j] != 0:
                flag = 1
                now_x = i
                now_y = j
                for y in range(n+1):
                    if new_bowl2[now_x - y][now_y] != 0:
                        new_fish[cnt] = new_bowl2[now_x - y][now_y]
                        cnt += 1
                    else:
                        break

        if flag == 1:
            break

    new_bowl3 = [[0]*(N//4) for _ in range(4)]

    new_bowl3[0] = new_fish[3*(N//4)-1:2*(N//4)-1:-1]
    new_bowl3[1] = new_fish[(N//4):2*(N//4)]
    new_bowl3[2] = new_fish[(N//4)-1::-1]
    new_bowl3[3] = new_fish[3*(N//4):N]

    newest_bowl = [[0]*(N//4) for _ in range(4)]
    for i in range(4):
        for j in range(N//4):
            newest_bowl[i][j] = new_bowl3[i][j]

    for i in range(4):
        for j in range(N//4):
            now_x, now_y = i, j
            for dir in direction:
                next_x = now_x + dir[0]
                next_y = now_y + dir[1]

                if 0 <= next_x < 4 and 0 <= next_y < N//4:
                    if new_bowl3[now_x][now_y] > new_bowl3[next_x][next_y]:
                        d = (new_bowl3[now_x][now_y] - new_bowl3[next_x][next_y])//5
                        newest_bowl[now_x][now_y] -= d
                        newest_bowl[next_x][next_y] += d

    sorted_fishes = [0] * N
    cnt = 0
    for i in range(N//4):
        for j in range(3, -1, -1):
            sorted_fishes[cnt] = newest_bowl[j][i]
            cnt += 1

    result = max(sorted_fishes) - min(sorted_fishes)
    turn += 1

print(turn)