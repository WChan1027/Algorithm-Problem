# https://www.acmicpc.net/problem/9328
import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline

T = int(input())
direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

for test_case in range(T):
    h, w = map(int, input().split())
    # 빌딩
    building = [list(map(str, input().strip())) for _ in range(h)]
    # 열쇠
    keys = list(map(str, input().strip()))
    # 방문 기록
    visited = [[0] * w for _ in range(h)]
    # 찾은 문서
    file = 0
    # 못 열어본 문
    lock = dict()

    start = deque()

    # 빌딩 가장자리 확인
    # 빌딩 순회
    for i in range(h):
        for j in range(w):
            # 빌딩 가장자리일 때
            if i == 0 or j == 0 or i == h-1 or j == w-1:
                # 통로일 때
                if building[i][j] == '.':
                    start.append((i, j))
                    visited[i][j] = 1

                # 벽일 때
                elif building[i][j] == '*':
                    visited[i][j] = 1

                # 서류일 때
                elif building[i][j] == '$':
                    file += 1
                    start.append((i, j))
                    visited[i][j] = 1

                # 문일 때
                elif building[i][j].isupper():
                    # 열쇠가 있으면
                    if building[i][j].lower() in keys:
                        start.append((i, j))
                        visited[i][j] = 1
                    # 열쇠가 없으면
                    else:
                        # 못 열어본 문 기록
                        if building[i][j].lower() in lock.keys():
                            lock[building[i][j].lower()].append((i, j))
                        else:
                            lock[building[i][j].lower()] = [(i, j)]

                # 열쇠일 때
                else:
                    # 새로운 열쇠일 때
                    if building[i][j] not in keys:
                        keys.append(building[i][j])
                    start.append((i, j))
                    visited[i][j] = 1

                    # 못 열어본 문 중 새로 주운 열쇠로 열 수 있는 곳이 있으면
                    if building[i][j] in lock.keys():
                        for open in lock[building[i][j]]:
                            open_x, open_y = open
                            start.append((open_x, open_y))
                            visited[open_x][open_y] = 1

    # 건물 내부 탐색
    while start:
        now_x, now_y = start.popleft()

        for dir in direction:
            next_x = now_x + dir[0]
            next_y = now_y + dir[1]

            if 0 <= next_x < h and 0 <= next_y < w and visited[next_x][next_y] == 0:
                # 통로일 때
                if building[next_x][next_y] == '.':
                    start.append((next_x, next_y))
                    visited[next_x][next_y] = 1

                # 벽일 때
                elif building[next_x][next_y] == '*':
                    visited[next_x][next_y] = 1

                # 문서일 때
                elif building[next_x][next_y] == '$':
                    file += 1
                    start.append((next_x, next_y))
                    visited[next_x][next_y] = 1

                # 문일 때
                elif building[next_x][next_y].isupper():
                    # 열쇠가 있으면
                    if building[next_x][next_y].lower() in keys:
                        start.append((next_x, next_y))
                        visited[next_x][next_y] = 1
                    # 열쇠가 없으면
                    else:
                        # 못 열어본 문 기록
                        if building[next_x][next_y].lower() in lock.keys():
                            lock[building[next_x][next_y].lower()].append((next_x, next_y))
                        else:
                            lock[building[next_x][next_y].lower()] = [(next_x, next_y)]

                # 열쇠일 때
                else:
                    # 새로운 열쇠일 때
                    if building[next_x][next_y] not in keys:
                        keys.append(building[next_x][next_y])
                    start.append((next_x, next_y))
                    visited[next_x][next_y] = 1

                    # 못 열어본 문 중 새로 주운 열쇠로 열 수 있는 곳이 있으면
                    if building[next_x][next_y] in lock.keys():
                        for open in lock[building[next_x][next_y]]:
                            open_x, open_y = open
                            start.append((open_x, open_y))
                            visited[open_x][open_y] = 1

    print(file)