# https://www.acmicpc.net/problem/1941
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

classroom1 = [list(input().strip()) for _ in range(5)]
classroom2 = dict()

n = 1

for i in range(5):
    for j in range(5):
        classroom2[n] = (i, j)
        n += 1

direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def check(i, j, k, l, m, n, o):
    global answer, direction

    cnt = 0
    if classroom1[classroom2[i][0]][classroom2[i][1]] == 'Y':
        cnt += 1
    if classroom1[classroom2[j][0]][classroom2[j][1]] == 'Y':
        cnt += 1
    if classroom1[classroom2[k][0]][classroom2[k][1]] == 'Y':
        cnt += 1
    if classroom1[classroom2[l][0]][classroom2[l][1]] == 'Y':
        cnt += 1
    if classroom1[classroom2[m][0]][classroom2[m][1]] == 'Y':
        cnt += 1
    if classroom1[classroom2[n][0]][classroom2[n][1]] == 'Y':
        cnt += 1
    if classroom1[classroom2[o][0]][classroom2[o][1]] == 'Y':
        cnt += 1

    if cnt > 3:
        return

    visited = [[0] * 5 for _ in range(5)]

    visited[classroom2[i][0]][classroom2[i][1]] = 1
    visited[classroom2[j][0]][classroom2[j][1]] = 1
    visited[classroom2[k][0]][classroom2[k][1]] = 1
    visited[classroom2[l][0]][classroom2[l][1]] = 1
    visited[classroom2[m][0]][classroom2[m][1]] = 1
    visited[classroom2[n][0]][classroom2[n][1]] = 1
    visited[classroom2[o][0]][classroom2[o][1]] = 1


    stack = [[classroom2[i][0], classroom2[i][1]]]

    checked = [[0] * 5 for _ in range(5)]
    checked[classroom2[i][0]][classroom2[i][1]] = 1
    cnt = 1

    while stack:
        now_x, now_y = stack.pop()

        for next in direction:
            next_x = now_x + next[0]
            next_y = now_y + next[1]

            if 0 <= next_x < 5 and 0 <= next_y < 5 and visited[next_x][next_y] == 1 and checked[next_x][next_y] == 0:
                checked[next_x][next_y] = 1
                stack.append([next_x, next_y])
                cnt += 1
    if cnt == 7:
        answer += 1

    return


answer = 0

for i in range(1, 20):
    for j in range(i+1, 21):
        for k in range(j+1, 22):
            for l in range(k+1, 23):
                for m in range(l+1, 24):
                    for n in range(m+1, 25):
                        for o in range(n+1, 26):
                            check(i, j, k, l, m, n, o)

print(answer)