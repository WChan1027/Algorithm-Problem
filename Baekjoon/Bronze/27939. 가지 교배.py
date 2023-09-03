import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())

color = list(map(str, input().split()))

m, k = map(int, input().split())

white = 0
for _ in range(m):
    egg_plants = list(map(int, input().split()))

    no = 0
    for egg_plant in egg_plants:
        if color[egg_plant-1] == 'P':
            no = 1
            break

    if no == 0:
        white += 1
        break

if white == 0:
    print('P')
else:
    print('W')