# https://www.acmicpc.net/problem/1991
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())

tree = [list(map(str, input().split())) for _ in range(N)]

def Front(now):
    print(now, end='')
    for i in range(N):
        if tree[i][0] == now:
            for child in tree[i][1:3]:
                if child != ".":
                    Front(child)
            return


def Middle(now):
    for i in range(N):
        if tree[i][0] == now:
            Middle(tree[i][1])
            print(now, end='')
            Middle(tree[i][2])

            return


def End(now):
    for i in range(N):
        if tree[i][0] == now:
            End(tree[i][1])
            End(tree[i][2])
            print(now, end='')

            return
Front('A')
print()
Middle('A')
print()
End('A')