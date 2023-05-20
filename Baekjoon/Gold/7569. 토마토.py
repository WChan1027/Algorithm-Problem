# https://www.acmicpc.net/problem/7569
import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline

M, N, H = map(int, input().split())

# 전체 상자
tomato = []

for _ in range(H):
    # 상자 한 층
    layer = [list(map(int, input().split())) for _ in range(N)]
    # 전체 상자에 추가
    tomato.append(layer)

# 익었는지 여부 체크. 숫자는 토마토가 익은 날짜
visited = [[[-1]*M for _ in range(N)] for _ in range(H)]
# 익은 토마토의 위치를 담을 que
que = deque()
# 익지 않은 토마토의 갯수
unripe = 0

# 상자를 순회
for h in range(H):
    for n in range(N):
        for m in range(M):
            # 익은 토마토의 위치를 que에 추가
            if tomato[h][n][m] == 1:
                que.append((h, n, m))
                visited[h][n][m] = 0
            # 토마토가 없는 위치는 1일째에 익은 것으로 체크
            elif tomato[h][n][m] == -1:
                visited[h][n][m] = 1
            # 익지 않은 토마토 +1
            else:
                unripe += 1

# 6가지 방향
direction = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]

# 안 익은 토마토가 0개면
if unripe == 0:
    # 0 출력
    print(0)
# 안 익은 토마토가 있으면
else:
    # 새로 익은 토마토 갯수
    count = 0
    while que:
        ripe_z, ripe_y, ripe_x = que.popleft()
        for i in range(6):
            next_ripe_z = ripe_z + direction[i][0]
            next_ripe_y = ripe_y + direction[i][1]
            next_ripe_x = ripe_x + direction[i][2]
            if 0 <= next_ripe_z < H and 0 <= next_ripe_y < N and 0 <= next_ripe_x < M:
                if visited[next_ripe_z][next_ripe_y][next_ripe_x] == -1:
                    que.append((next_ripe_z, next_ripe_y, next_ripe_x))
                    visited[next_ripe_z][next_ripe_y][next_ripe_x] = visited[ripe_z][ripe_y][ripe_x] + 1
                    count += 1

    # 새로 익은 토마토 갯수와 안 익었던 토마토 갯수가 같으면
    # 전부 익었으므로 마지막 토마토가 익은 날짜 출력
    if count == unripe:
        print(visited[ripe_z][ripe_y][ripe_x])
    # 둘의 갯수가 다르면 익지 못하는 토마토가 있다는 뜻이므로
    # -1 출력
    else:
        print(-1)