import sys

sys.stdin = open('sample_input.txt')

T = int(input())

def bfs(cp):
    stack = [cp]
    visited[cp[0]][cp[1]] = 0

    while stack:
        check = stack.pop(0)

        for i in range(4):
            next = [check[0] + direction[i][0], check[1] + direction[i][1]]
            if 0 <= next[0] < N and 0 <= next[1] < N:
                if maze[next[0]][next[1]] == 3:
                    return visited[check[0]][check[1]]
                elif visited[next[0]][next[1]] == 0:
                    stack.append(next)
                    visited[next[0]][next[1]] = visited[check[0]][check[1]] + 1

    return 0

for test_case in range(1, T+1):
    N = int(input())
    maze = []

    for _ in range(N):
        maze += [list(int(i) for i in input())]

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                sp = [i, j]
                break

    direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    visited = [_[:] for _ in maze]

    print(f'#{test_case} {bfs(sp)}')