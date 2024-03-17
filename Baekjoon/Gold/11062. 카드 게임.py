import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

T = int(input())

# play(남은 카드의 왼쪽 좌표, 남은 카드의 오른쪽 좌표, 순서)
# turn : True(명우), False(근우)
def play(i, j, turn):
    # 선택할 카드가 없을 때
    if i > j:
        return 0

    # 이미 계산한 경우일 때
    if dp[i][j]:
        return dp[i][j]

    # score : 명우의 점수
    # 해당 카드들이 선택되는 경우 명우 점수의 최대값
    if turn:
        score = max(play(i+1, j, not turn) + cards[i], play(i, j-1, not turn) + cards[j])
    # 해당 카드들이 선택되는 경우 명우 점수의 최솟값
    else:
        score = min(play(i+1, j, not turn), play(i, j-1, not turn))

    dp[i][j] = score

    return score


for test_case in range(T):
    N = int(input())
    cards = list(map(int, input().split()))
    dp = list([0]*N for _ in range(N))

    print(play(0, N-1, True))