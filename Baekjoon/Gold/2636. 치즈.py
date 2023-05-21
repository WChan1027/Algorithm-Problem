import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline

n, m = map(int, input().split())

cheeze = [list(map(int, input().split())) for _ in range(n)]

# 해당 위치가 녹는 시간을 기록
visited = [[-1] * m for _ in range(n)]
direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

que = deque()
que.append((0, 0))
visited[0][0] = 0

# BFS
while que:
    (now_x, now_y) = que.popleft()

    for dir in direction:
        next_x, next_y = now_x + dir[0], now_y + dir[1]

        if 0 <= next_x < n and 0 <= next_y < m:
            # 치즈가 없는 공간일 때
            if cheeze[next_x][next_y] == 0:
                # 방문한 적 없거나, 더 빠른 시간에 방문할 수 있다면
                if visited[next_x][next_y] == -1 or visited[next_x][next_y] > visited[now_x][now_y]:
                    # 방문 시간 기록
                    visited[next_x][next_y] = visited[now_x][now_y]
                    que.append((next_x, next_y))
            # 치즈가 있는 공간일 때
            elif cheeze[next_x][next_y] == 1:
                # 방문한 적 없거나, 더 빠른 시간에 녹을 수 있다면
                if visited[next_x][next_y] == -1 or visited[next_x][next_y] > visited[now_x][now_y]+1:
                    # 녹는 시간 기록
                    visited[next_x][next_y] = visited[now_x][now_y] + 1
                    que.append((next_x, next_y))

# 녹은 시간 중 최댓값
time = max(max(visited[i]) for i in range(n))
# 가장 마지막에 녹은 치즈조각의 수
cnt = 0
for i in range(n):
    for j in range(m):
        if visited[i][j] == time and cheeze[i][j] == 1:
            cnt += 1

print(time)
print(cnt)