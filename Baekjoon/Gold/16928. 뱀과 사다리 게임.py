import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())

board = [100] * 101
move = dict()
for _ in range(N + M):
    x, y = map(int, input().split())
    move[x] = y

queue = deque()
queue.append(1)
board[1] = 0

while queue:
    now = queue.popleft()
    for i in range(1, 7):
        next = now + i
        if next < 100:
            if next in move.keys():
                next = move[next]
            if board[now] + 1 < board[next]:
                board[next] = board[now] + 1
                queue.append(next)
        elif next >= 100:
            board[100] = board[now] + 1
            queue = []
            break

print(board[100])