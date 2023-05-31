# https://www.acmicpc.net/problem/1967
import sys
from collections import defaultdict
sys.stdin = open('input.txt')
input = sys.stdin.readline

# 임의의 정점 A에서 다른 정점들까지의 거리를 모두 구한다
# A에서 가장 멀리 있는 정점 S를 시작점으로 다른 정점들까지의 거리를 모두 구한다.
# S에서 가장 멀리 있는 정점 E까지의 거리가 트리의 지름이다.

n = int(input())
graph = defaultdict(list)
answer = 0

# 시간초과를 막기 위해 이차원 리스트가 아닌 dict 형태로 간선 정보 저장
for case in range(n-1):
    S, E, T = list(map(int, input().split()))

    graph[S] += [(E, T)]
    graph[E] += [(S, T)]

def BFS(start):
    global answer
    visited = [float('INF')] * (n + 1)
    stack = [(start, 0)]
    visited[start] = 0

    while stack:
        now, time = stack.pop()

        for next in graph[now]:
            if next[1] + time < visited[next[0]]:
                visited[next[0]] = next[1] + time
                stack.append((next[0], next[1] + time))

    result = max(visited[1:])
    answer = max(result, answer)

    for i in range(1, n+1):
        if visited[i] == result:
            return i

BFS(BFS(1))

print(answer)