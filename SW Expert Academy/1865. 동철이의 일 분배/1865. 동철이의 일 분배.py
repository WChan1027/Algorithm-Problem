import sys
sys.stdin = open('input.txt')

T = int(input())

def backtrack(a, n, percent):
    global answer
    if percent <= answer:
        return

    if a == n:
        for i in range(N):
            if not visited[i]:
                percent = percent * success[a][i]
        if percent > answer:
            answer = percent
            return

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            if percent * success[a][i] >= answer:
                backtrack(a+1, n, percent * success[a][i])
            visited[i] = False

for test_case in range(1, T+1):
    N = int(input())
    success = []
    answer = 1
    visited = [False] * N

    for _ in range(N):
        success.append(list(map(float, input().split())))

    for i in range(N):
        for j in range(N):
            success[i][j] = success[i][j] / 100

    for i in range(N):
        answer *= success[i][i]

    backtrack(0, N, 100)

    print(f'#{test_case} {answer:.6f}')