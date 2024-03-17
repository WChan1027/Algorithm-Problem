import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def solution(N, picture):
    direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def area_normal(picture):
        visited = [[0] * N for _ in range(N)]
        cnt = 0
        for i in range(N):
            for j in range(N):
                if not visited[i][j]:
                    cnt += 1
                    color = picture[i][j]
                    stack = [(i, j)]
                    visited[i][j] = 1
                    while stack:
                        now_x, now_y = stack.pop()
                        for d_x, d_y in direction:
                            next_x, next_y = now_x + d_x, now_y + d_y
                            if 0 <= next_x < N and 0 <= next_y < N and not visited[next_x][next_y] and picture[next_x][next_y] == color:
                                visited[next_x][next_y] = 1
                                stack.append((next_x, next_y))

        return cnt

    def area_color(picture):
        visited = [[0] * N for _ in range(N)]
        cnt = 0
        for i in range(N):
            for j in range(N):
                if not visited[i][j]:
                    cnt += 1
                    color = picture[i][j]
                    stack = [(i, j)]
                    visited[i][j] = 1
                    if color == 'B':
                        while stack:
                            now_x, now_y = stack.pop()
                            for d_x, d_y in direction:
                                next_x, next_y = now_x + d_x, now_y + d_y
                                if 0 <= next_x < N and 0 <= next_y < N and not visited[next_x][next_y] and picture[next_x][next_y] == color:
                                    visited[next_x][next_y] = 1
                                    stack.append((next_x, next_y))
                    else:
                        while stack:
                            now_x, now_y = stack.pop()
                            for d_x, d_y in direction:
                                next_x, next_y = now_x + d_x, now_y + d_y
                                if 0 <= next_x < N and 0 <= next_y < N and not visited[next_x][next_y] and picture[next_x][next_y] != 'B':
                                    visited[next_x][next_y] = 1
                                    stack.append((next_x, next_y))
        return cnt

    print(area_normal(picture), area_color(picture))
    return

N = int(input())
picture = [list(map(str, input().strip())) for _ in range(N)]

solution(N, picture)