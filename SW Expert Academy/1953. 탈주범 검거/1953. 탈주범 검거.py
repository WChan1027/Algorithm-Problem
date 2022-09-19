import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for test_case in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    tunnel = []
    for _ in range(N):
        tunnel.append(list(map(int, input().split())))

    maze = [[0]*M for _ in range(N)]

    stack = [[R, C]]
    maze[R][C] = 1
    while stack:
        [x, y] = stack.pop(0)
        if tunnel[x][y] == 1:
            if y < M-1 and tunnel[x][y+1] in [1, 3, 6, 7] and maze[x][y+1] == 0:
                stack.append([x, y+1])
                maze[x][y+1] = maze[x][y] + 1
            if x < N-1 and tunnel[x+1][y] in [1, 2, 4, 7] and maze[x+1][y] == 0:
                stack.append([x+1, y])
                maze[x+1][y] = maze[x][y] + 1
            if y > 0 and tunnel[x][y-1] in [1, 3, 4, 5] and maze[x][y-1] == 0:
                stack.append([x, y-1])
                maze[x][y-1] = maze[x][y] + 1
            if x > 0 and tunnel[x-1][y] in [1, 2, 5, 6] and maze[x-1][y] == 0:
                stack.append([x-1, y])
                maze[x-1][y] = maze[x][y] + 1

        elif tunnel[x][y] == 2:
            if x < N-1 and tunnel[x+1][y] in [1, 2, 4, 7] and maze[x+1][y] == 0:
                stack.append([x+1, y])
                maze[x+1][y] = maze[x][y] + 1
            if x > 0 and tunnel[x-1][y] in [1, 2, 5, 6] and maze[x-1][y] == 0:
                stack.append([x-1, y])
                maze[x-1][y] = maze[x][y] + 1

        elif tunnel[x][y] == 3:
            if y < M-1 and tunnel[x][y+1] in [1, 3, 6, 7] and maze[x][y+1] == 0:
                stack.append([x, y+1])
                maze[x][y+1] = maze[x][y] + 1
            if y > 0 and tunnel[x][y-1] in [1, 3, 4, 5] and maze[x][y-1] == 0:
                stack.append([x, y-1])
                maze[x][y-1] = maze[x][y] + 1

        elif tunnel[x][y] == 4:
            if y < M-1 and tunnel[x][y+1] in [1, 3, 6, 7] and maze[x][y+1] == 0:
                stack.append([x, y+1])
                maze[x][y+1] = maze[x][y] + 1
            if x > 0 and tunnel[x-1][y] in [1, 2, 5, 6] and maze[x-1][y] == 0:
                stack.append([x-1, y])
                maze[x-1][y] = maze[x][y] + 1

        elif tunnel[x][y] == 5:
            if y < M-1 and tunnel[x][y+1] in [1, 3, 6, 7] and maze[x][y+1] == 0:
                stack.append([x, y+1])
                maze[x][y+1] = maze[x][y] + 1
            if x < N-1 and tunnel[x+1][y] in [1, 2, 4, 7] and maze[x+1][y] == 0:
                stack.append([x+1, y])
                maze[x+1][y] = maze[x][y] + 1

        elif tunnel[x][y] == 6:
            if x < N-1 and tunnel[x+1][y] in [1, 2, 4, 7] and maze[x+1][y] == 0:
                stack.append([x+1, y])
                maze[x+1][y] = maze[x][y] + 1
            if y > 0 and tunnel[x][y-1] in [1, 3, 4, 5] and maze[x][y-1] == 0:
                stack.append([x, y-1])
                maze[x][y-1] = maze[x][y] + 1

        elif tunnel[x][y] == 7:
            if y > 0 and tunnel[x][y-1] in [1, 3, 4, 5] and maze[x][y-1] == 0:
                stack.append([x, y-1])
                maze[x][y-1] = maze[x][y] + 1
            if x > 0 and tunnel[x-1][y] in [1, 2, 5, 6] and maze[x-1][y] == 0:
                stack.append([x-1, y])
                maze[x-1][y] = maze[x][y] + 1

    answer = 0
    for i in range(N):
        for j in range(M):
            if 0 < maze[i][j] <= L:
                answer += 1

    print(f'#{test_case} {answer}')