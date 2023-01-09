# https://www.acmicpc.net/problem/1992
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())

video = [list(map(str, input().strip())) for _ in range(N)]
answer = ''

def check(x, y, N):
    global answer
    spot = video[x][y]
    same = 1
    for i in range(x, x + N):
        for j in range(y, y + N):
            if video[i][j] != spot:
                same = 0
                break
        if same == 0:
            break

    if same == 0:
        answer += '('
        check(x, y, N//2)
        check(x, y + N//2, N//2)
        check(x + N//2, y, N//2)
        check(x + N//2, y + N//2, N//2)
        answer += ')'

    else:
        answer += spot

check(0, 0, N)

print(answer)