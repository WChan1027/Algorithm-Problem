# https://www.acmicpc.net/problem/17144
import sys
import copy
sys.stdin = open('input.txt')
input = sys.stdin.readline

R, C, T = map(int, input().split())

room = [list(map(int, input().split())) for _ in range(R)]
cleaner = []
for i in range(R):
    if room[i][0] == -1:
        cleaner.append(i)

clock = cleaner[1]
clock_reverse = cleaner[0]

direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def diffusion():
    global R, C, clock, clock_reverse, room
    new_room = copy.deepcopy(room)
    for x in range(R):
        for y in range(C):
            if room[x][y] > 0:
                cnt = 0
                for dir in direction:
                    next_x, next_y = x + dir[0], y + dir[1]
                    if 0 <= next_x < R and 0 <= next_y < C and room[next_x][next_y] > -1:
                        new_room[next_x][next_y] += room[x][y] // 5
                        cnt += 1

                new_room[x][y] -= (room[x][y] // 5) * cnt

    room = new_room

    new_room = copy.deepcopy(room)

    new_room[clock][1] = 0
    new_room[clock_reverse][1] = 0

    for i in range(2, C):
        new_room[clock][i] = room[clock][i-1]
        new_room[clock_reverse][i] = room[clock_reverse][i-1]

    for i in range(C-1):
        new_room[0][i] = room[0][i+1]
        new_room[R-1][i] = room[R-1][i+1]

    for i in range(clock+1, R):
        new_room[i][C-1] = room[i-1][C-1]

    for i in range(clock_reverse):
        new_room[i][C-1] = room[i + 1][C-1]

    for i in range(1, clock_reverse):
        new_room[i][0] = room[i - 1][0]

    for i in range(clock+1, R-1):
        new_room[i][0] = room[i + 1][0]

    return new_room



for time in range(T):
    room = diffusion()

dust = 0
for i in range(R):
    for j in range(C):
        if room[i][j] > 0:
            dust += room[i][j]

print(dust)
for a in room:
    print(*a)
