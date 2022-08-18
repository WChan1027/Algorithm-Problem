import sys

sys.stdin = open('sample_input.txt')

# DFS
def DFS(start, goal):
    visited[start] = 1
    # goal에 도달하면 함수 바깥에 흔적을 남김
    if start == goal:
        result.append(1)

    for next in range(1, V+1):
        if graph[start][next] == 1 and visited[next] == 0:
            DFS(next, goal)


T = int(input())

for test_case in range(1, T+1):
    V, E = map(int, input().split())

    graph = [[0 for _ in range(V+1)] for _ in range(V+1)]
    visited = [0] * (V+1)

    for _ in range(E):
        S, G = map(int, input().split())
        graph[S][G] = 1

    start, goal = map(int, input().split())
    result = []

    DFS(start, goal)
    # start에서 출발해 goal에 도착해 흔적을 남겼는지 확인
    answer = 0 if len(result) == 0 else 1

    print(f'#{test_case} {answer}')