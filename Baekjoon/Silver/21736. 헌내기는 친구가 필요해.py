import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(str, input().strip())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

for i in range(N):
    for j in range(M):
        if graph[i][j] == 'I':
            start_x, start_y = i, j
            break
    else:
        continue
    break

queue = [(start_x, start_y)]
visited[start_x][start_y] = 1
answer = 0

while queue:
    now_x, now_y = queue.pop()
    for d in direction:
        next_x, next_y = now_x + d[0], now_y + d[1]
        if 0 <= next_x < N and 0 <= next_y < M:
            if visited[next_x][next_y] == 0:
                if graph[next_x][next_y] == 'X':
                    continue
                elif graph[next_x][next_y] == 'P':
                    answer += 1
                visited[next_x][next_y] = 1
                queue.append((next_x, next_y))

print('TT') if answer == 0 else print(answer)