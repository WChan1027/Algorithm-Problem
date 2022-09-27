import sys
sys.stdin = open('sample_input.txt')

T = int(input())

def go(x, y, N):
    global answer
    if sum(result) > answer:
        return

    if x < N - 1:
        result.append(board[x][y])
        go(x + 1, y, N)
        result.pop()

    if y < N - 1:
        result.append(board[x][y])
        go(x, y + 1, N)
        result.pop()

    if len(result) == 2 * N - 1 and sum(result) < answer:
        answer = sum(result)
        return

for test_case in range(1, T+1):
    N = int(input())
    board = []
    answer = 10*(2*N-1)
    for _ in range(N):
        board.append(list(map(int, input().split())))

    x, y = 0, 0
    result = [board[N-1][N-1]]

    go(x, y, N)

    print(f'#{test_case} {answer}')