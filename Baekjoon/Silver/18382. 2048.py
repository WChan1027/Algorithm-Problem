'''
https://www.acmicpc.net/problem/18382

[문제]

2048 is a sliding block puzzle game.
The game's objective is to slide numbered tiles on a grid to combine them to create a tile with the number 2048.
It is played on a 4×4 grid, with numbered tiles that slide smoothly when the player moves them using the four arrow keys.
Every turn, a new tile will randomly appear in an empty spot on the board with a value of either 2 or 4.
Tiles slide as far as possible in the chosen direction until they are stopped by either another tile or the edge of the grid.
If two tiles of the same number collide while moving, they will merge into a tile with the total value of the two tiles that collided.
The resulting tile cannot merge with another tile again in the same move.
The user's score starts at zero, and is incremented whenever two tiles combine, by the value of the new tile.

Write a program that takes the current user score,
M number of moves and random appeared numbers (and their location on grid) and the current grid values as inputs and print the final score of the user.

'''
import sys
S = int(sys.stdin.readline())

move = list(sys.stdin.readline())

grid = list(map(int, sys.stdin.readline().split()))

puzzle = [[0]*4 for i in range(4)]

# 퍼즐 최초 상태
n = 0
for i in range(4):
    for j in range(4):
        puzzle[i][j] = grid[n]
        n += 1

# Left
def move_left(puzzle):
    plus = 0        # 얻은 점수
    for i in range(4):      # 행 선택
        idx = 0         # 쌓이는 가장 아래쪽
        for j in range(1, 4):       # 선택된 행의 가장 아래쪽+1 부터 확인
            if puzzle[i][j] != 0:       # 퍼즐이 비어있지 않으면
                if idx != j:        # 현재 위치 != 쌓을 위치면
                    if puzzle[i][idx] == puzzle[i][j]:      # 현재 선택된 퍼즐과 쌓을 위치의 퍼즐의 숫자가 같으면
                        puzzle[i][idx] *= 2     # 쌓을 위치의 숫자 * 2
                        puzzle[i][j] = 0        # 현재 선택된 퍼즐 위치 비우기
                        plus += puzzle[i][idx]      # 점수 추가
                        idx += 1        # 쌓을 위치 +1
                    elif puzzle[i][idx] == 0:       # 쌓을 위치의 숫자가 0이면
                        puzzle[i][idx] = puzzle[i][j]       # 현재 선택된 퍼즐을 쌓을 위치로 이동
                        puzzle[i][j] = 0        # 현재 선택된 퍼즐 위치 비우기
                    else:       # 현재 선택된 퍼즐과 쌓을 위치의 퍼즐의 숫자가 같지 않으면
                        idx += 1        # 쌓을 위치 +1
                        puzzle[i][idx] = puzzle[i][j]       # 현재 선택된 퍼즐을 쌓을 위치로 이동
                        if idx != j:        # 현재 위치 != 쌓을 위치면
                            puzzle[i][j] = 0        # 현재 선택된 퍼즐 위치 비우기
    return plus     # 얻은 점수 반환

# Up
def move_up(puzzle):
    plus = 0
    for j in range(4):
        idx = 0
        for i in range(1, 4):
            if puzzle[i][j] != 0:
                if idx != i:
                    if puzzle[idx][j] == puzzle[i][j]:
                        puzzle[idx][j] *= 2
                        puzzle[i][j] = 0
                        plus += puzzle[idx][j]
                        idx += 1
                    elif puzzle[idx][j] == 0:
                        puzzle[idx][j] = puzzle[i][j]
                        puzzle[i][j] = 0
                    else:
                        idx += 1
                        puzzle[idx][j] = puzzle[i][j]
                        if idx != i:
                            puzzle[i][j] = 0
    return plus

# Right
def move_right(puzzle):
    plus = 0
    for i in range(4):
        idx = 3
        for j in range(2, -1, -1):
            if puzzle[i][j] != 0:
                if idx != j:
                    if puzzle[i][idx] == puzzle[i][j]:
                        puzzle[i][idx] *= 2
                        puzzle[i][j] = 0
                        plus += puzzle[i][idx]
                        idx -= 1
                    elif puzzle[i][idx] == 0:
                        puzzle[i][idx] = puzzle[i][j]
                        puzzle[i][j] = 0
                    else:
                        idx -= 1
                        puzzle[i][idx] = puzzle[i][j]
                        if idx != j:
                            puzzle[i][j] = 0
    return plus

# Down
def move_down(puzzle):
    plus = 0
    for j in range(4):
        idx = 3
        for i in range(2, -1, -1):
            if puzzle[i][j] != 0:
                if idx != i:
                    if puzzle[idx][j] == puzzle[i][j]:
                        puzzle[idx][j] *= 2
                        puzzle[i][j] = 0
                        plus += puzzle[idx][j]
                        idx -= 1
                    elif puzzle[idx][j] == 0:
                        puzzle[idx][j] = puzzle[i][j]
                        puzzle[i][j] = 0
                    else:
                        idx -= 1
                        puzzle[idx][j] = puzzle[i][j]
                        if idx != i:
                            puzzle[i][j] = 0
    return plus

index = -1      # 순회할 move 위치
while index < len(move)-1:      # move가 끝날 때까지 반복
    index += 1      # move 위치 +1
    # 4개마다 명령 반복
    if index % 4 == 0:      # 이동할 방향에 따라 함수 실행 
        if move[index] == 'L':
            S += move_left(puzzle)
        elif move[index] == 'U':
            S += move_up(puzzle)
        elif move[index] == 'R':
            S += move_right(puzzle)
        else:
            S += move_down(puzzle)

    elif index % 4 == 1:        # 새로 생길 숫자의 크기
        num = int(move[index])
    elif index % 4 == 2:        # 새로 생길 숫자의 행 좌표
        column = int(move[index])
    else:       # 새로 생길 숫자의 열 좌표
        row = int(move[index])
        puzzle[column][row] = num       # puzzle에 새로운 숫자 등록

print(S)