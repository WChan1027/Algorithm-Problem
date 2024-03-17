def solution(board, aloc, bloc):
    direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    row = len(board)
    col = len(board[0])

    def next_move(board, player):
        result = []
        for d in direction:
            next = [player[0] + d[0], player[1] + d[1]]
            if 0 <= next[0] < row and 0 <= next[1] < col and board[next[0]][next[1]]:
                result.append(next)
        return result

    def play(board, aloc, bloc, turn):
        if turn % 2:
            now = bloc
        else:
            now = aloc

        next = next_move(board, now)
        if not next:
            return (1, turn) if turn % 2 else (-1, turn)

        if aloc == bloc:
            return (-1, turn+1) if turn % 2 else (1, turn+1)

        min_turn = float('inf')
        max_turn = float('-inf')

        if now == aloc:
            value = -1
            for n in next:
                board[now[0]][now[1]] = 0
                result = play(board, n, bloc, turn + 1)
                board[now[0]][now[1]] = 1

                if result[0] == 1:
                    value = result[0]
                    min_turn = min(min_turn, result[1])
                else:
                    max_turn = max(max_turn, result[1])
            if value == 1:
                return (1, min_turn)
            else:
                return (-1, max_turn)
        else:
            value = 1
            for n in next:
                board[now[0]][now[1]] = 0
                result = play(board, aloc, n, turn + 1)
                board[now[0]][now[1]] = 1

                if result[0] == -1:
                    value = result[0]
                    min_turn = min(min_turn, result[1])
                else:
                    max_turn = max(max_turn, result[1])
            if value == -1:
                return (-1, min_turn)
            else:
                return (1, max_turn)


    answer = play(board, aloc, bloc, 0)[1]

    return answer