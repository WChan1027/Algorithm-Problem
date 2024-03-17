import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


# 게임 종료 확인
def is_end(board, player):
    # 승리시 1, 패배시 -1, 무승부시 0 반환
    for i in range(3):
        if board[0][i] != 0 and board[0][i] == board[1][i] and board[1][i] == board[2][i]:
            if board[0][i] == player:
                return 1
            else:
                return -1

    for i in range(3):
        if board[i] == [1, 1, 1]:
            if player == 1:
                return 1
            else:
                return -1
        elif board[i] == [2, 2, 2]:
            if player == 2:
                return 1
            else:
                return -1

    if board[0][0] != 0 and board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        if board[0][0] == player:
            return 1
        else:
            return -1

    if board[2][0] != 0 and board[2][0] == board[1][1] and board[1][1] == board[0][2]:
        if board[2][0] == player:
            return 1
        else:
            return -1

    # 빈칸이 아직 있으면 게임 속행
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                return -2

    # 게임이 끝났는데 승자가 없으면 무승부 반환
    return 0


# 게임 실행
def play(board, player_start, player):
    result = is_end(board, player_start)
    if result != -2:
        return result

    # 기준이 되는 플레이어라면 최선의 값을 선택
    if player == player_start:
        value = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:
                    board[i][j] = player
                    value = max(value, play(board, player_start, 3 - player))
                    board[i][j] = 0

    # 상대 플레이어라면 최악의 값을 선택
    else:
        value = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:
                    board[i][j] = player
                    value = min(value, play(board, player_start, 3 - player))
                    board[i][j] = 0

    return value


# 현재 어느 플레이어의 차례인지 확인
def start_turn(board):
    turn = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] != 0:
                turn += 1

    return 1 if turn % 2 == 0 else 2


board = list(list(map(int, input().split())) for _ in range(3))
player_start = start_turn(board)

answer = play(board, player_start, player_start)

if answer == 0:
    print('D')
elif answer == 1:
    print('W')
else:
    print('L')
