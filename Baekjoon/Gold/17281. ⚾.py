import sys
import itertools

sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())

players = list(range(9))
result = [list(map(int, input().split())) for _ in range(N)]

players_comb = list(itertools.permutations(players, 9))
answer = 0

for order in players_comb:
