import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline

R, C = map(int, input().split())

parking_lot = list(input().strip() for _ in range(R))

def is_valid_move(x, y, grid):
    rows, cols = len(grid), len(grid[0])
    return 0 <= x < rows and 0 <= y < cols and grid[x][y] != 'X'

def min_parking_time(matrix, cars, parking):
    global R, C
    que = deque([(x, y, 0) for x, y in cars])
    visited = set(cars)

    while que:
        x, y, time = que.popleft()

        if (x, y) in parking:
            parking.remove((x, y))
            if not parking:
                return time

        for dir in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            next_x, next_y = x + dir[0], y + dir[1]
            if is_valid_move(next_x, next_y, matrix) and (next_x, next_y) not in visited:
                visited.add((next_x, next_y))
                que.append((next_x, next_y, time + 1))

    return -1

cars = []
parking = []

for i in range(R):
    for j in range(C):
        if parking_lot[i][j] == 'C':
            cars.append((i, j))
        elif parking_lot[i][j] == 'P':
            parking.append((i, j))

result = min_parking_time(parking_lot, cars, parking)
print(result)

print()