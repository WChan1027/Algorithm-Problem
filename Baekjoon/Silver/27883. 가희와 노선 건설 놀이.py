import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n, m = map(int, input().split())

turn = 0
height = 0

act = []
act.append(['U', 1, -1])
turn += 1

for _ in range(m):
    answer = int(input())

    act.append(['U', answer+1, height+1])
    height += 1
    turn += 1

    act.append(['P'])
    turn += 1

print(turn)

for a in act:
    print(*a)