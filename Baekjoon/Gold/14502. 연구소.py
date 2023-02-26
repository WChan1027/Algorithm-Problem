# https://www.acmicpc.net/problem/14502
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())

lab = [list(map(int, input().split())) for _ in range(N)]


direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
answer = 0

def wall(n):
    global answer
    if n == 3:
        lab_after = [[0] * M for _ in range(N)]
        for i in range(N):
            for j in range(M):
                lab_after[i][j] = lab[i][j]

        safe = 0
        stack = []
        for i in range(N):
            for j in range(M):
                if lab[i][j] == 2:
                    stack.append((i, j))
                elif lab[i][j] == 0:
                    safe += 1

        while stack:
            now_x, now_y = stack.pop()

            for dir in direction:
                next_x = now_x + dir[0]
                next_y = now_y + dir[1]

                if 0 <= next_x < N and 0 <= next_y < M and lab_after[next_x][next_y] == 0:
                    lab_after[next_x][next_y] = 2
                    stack.append((next_x, next_y))
                    safe -= 1

        if safe > answer:
            answer = safe
        return

    for i in range(N):
        for j in range(M):
            if lab[i][j] == 0:
                lab[i][j] = 1
                wall(n+1)
                lab[i][j] = 0

wall(0)

print(answer)