import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

egg_plant = list(list(map(str, input().split())) for _ in range(10))

answer = 0
for i in range(10):
    if egg_plant[i].count(egg_plant[i][0]) == 10:
        answer = 1
        break

    color = egg_plant[0][i]
    for j in range(1, 10):
        if egg_plant[j][i] != color:
            break
    else:
        answer = 1
        break

print(answer)