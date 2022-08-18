import sys

sys.stdin = open('input.txt')

# DFS
def DFS(start, goal):
    visited[start] = 1
    print(start, goal)
    # goal 지점에 도달하면 함수 바깥의 result에 흔적을 남김
    if start == goal:
        result.append(1)

    for next in range(100):
        if graph[start][next] == 1 and visited[next] == 0:
            DFS(next, goal)

for test_case in range(10):
    T, E = map(int, input().split())
    path = list(map(int, input().split()))

    graph = [[0] * 100 for _ in range(100)]
    visited = [0] * 100
    result = []

    for i in range(E):
        graph[path[2*i]][path[2*i + 1]] = 1

    DFS(0, 99)
    # result에 goal 지점에 도달한 흔적이 있으면 1, 아니면 0
    answer = 0 if len(result) == 0 else 1

    print(f'#{T} {answer}')