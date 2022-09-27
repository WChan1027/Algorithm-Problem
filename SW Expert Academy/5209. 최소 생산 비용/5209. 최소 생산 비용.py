import sys
sys.stdin = open('sample_input.txt')

T= int(input())

def backtrack(a, n):
    global answer
    if a == n:
        for i in range(n):
            if not visited[i]:
                result.append(cost_factory[a][i])
        if sum(result) < answer:
            answer = sum(result)
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            result.append(cost_factory[a][i])
            if sum(result) < answer:
                backtrack(a+1, n)
            visited[i] = False
            result.pop()

for test_case in range(1, T+1):
    N = int(input())
    cost_factory = []
    for _ in range(N):
        cost_factory.append(list(map(int, input().split())))

    result = []
    answer = 0
    for i in range(N):
        answer += cost_factory[i][i]

    visited = [False] * N

    backtrack(0, N)

    print(f'#{test_case} {answer}')