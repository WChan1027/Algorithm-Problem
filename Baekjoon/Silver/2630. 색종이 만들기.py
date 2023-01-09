# https://www.acmicpc.net/problem/2630
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())

paper = [list(map(int, input().split())) for _ in range(N)]

answer = [0, 0]
def check(x, y, N):
    color = paper[x][y]
    same = 1
    for i in range(x, x + N):
        for j in range(y, y + N):
            if paper[i][j] != color:
                same = 0
                break
        if same == 0:
            break

    if same == 0:
        check(x, y, N//2)
        check(x, y + N//2, N//2)
        check(x + N//2, y, N//2)
        check(x + N//2, y + N//2, N//2)

    else:
        answer[color] += 1

check(0, 0, N)

print(answer[0])
print(answer[1])