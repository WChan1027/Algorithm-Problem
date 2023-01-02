# https://www.acmicpc.net/problem/1780
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
answer = {-1:0, 0:0, 1:0}

def check(N, start):
    x, y = start
    a = paper[x][y]
    for i in range(N):
        for j in range(N):
            if paper[x+i][y+j] != a:
                cut(N, start)
                return
    answer[a] += 1
    return

def cut(N, start):
    x, y = start
    check(N//3, [x, y])
    check(N//3, [x + N//3, y])
    check(N//3, [x + N//3 + N//3, y])
    check(N//3, [x, y + N//3])
    check(N//3, [x + N//3, y + N//3])
    check(N//3, [x + N//3 + N//3, y + N//3])
    check(N//3, [x, y + N//3 + N//3])
    check(N//3, [x + N//3, y + N//3 + N//3])
    check(N//3, [x + N//3 + N//3, y + N//3 + N//3])
    return

check(N, [0, 0])
print(answer[-1])
print(answer[0])
print(answer[1])