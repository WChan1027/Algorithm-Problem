# https://www.acmicpc.net/problem/14615
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())

tube = dict()
tube_reverse = dict()

for _ in range(M):
    X, Y = map(int, input().split())

    if X in tube.keys():
        tube[X] += [Y]
    else:
        tube[X] = [Y]

    if Y in tube_reverse.keys():
        tube_reverse[Y] += [X]
    else:
        tube_reverse[Y] = [X]

stack = [1]
visited = [0] * (N+1)
visited[1] = 1
find_bomb = [1]

while stack:
    now = stack.pop()

    if now in tube.keys():
        for next in tube[now]:
            if visited[next] == 0:
                visited[next] = 1
                stack.append(next)
                find_bomb.append(next)

stack = [N]
visited = [0] * (N+1)
visited[N] = 1
throw_bomb = [N]

while stack:
    now = stack.pop()

    if now in tube_reverse.keys():
        for next in tube_reverse[now]:
            if visited[next] == 0:
                visited[next] = 1
                stack.append(next)
                throw_bomb.append(next)


T = int(input())

for num in range(T):
    bomb = int(input())

    if bomb in find_bomb and bomb in throw_bomb:
        print('Defend the CTP')
    else:
        print('Destroyed the CTP')