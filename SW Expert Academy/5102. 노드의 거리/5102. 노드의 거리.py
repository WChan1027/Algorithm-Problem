import sys

sys.stdin = open('sample_input.txt')

T = int(input())

def bfs(S, G):      # bfs
    visited[S] = 1
    stack = [S]

    while stack:        # 방문한 곳에 +1씩
        now = stack.pop(0)
        for next in range(V+1):
            if graph[now][next] == 1 and visited[next] == 0:
                visited[next] = visited[now] + 1
                stack.append(next)
                if next == G:
                    return visited[now]
    return 0

for test_case in range(1, T+1):
    V, E = map(int, input().split())
    line = list()
    for _ in range(E):
        line += [list(map(int, input().split()))]
    S, G = map(int, input().split())

    graph = [[0]*(V+1) for i in range(V+1)]

    for i in line:
        graph[i[0]][i[1]] = 1
        graph[i[1]][i[0]] = 1

    visited = [0] * (V+1)

    answer = bfs(S, G)

    print(f'#{test_case} {answer}')