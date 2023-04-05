# https://www.acmicpc.net/problem/22941
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

HP, ATK, HP_Boss, ATK_Boss = map(int, input().split())

P, S = map(int, input().split())

turn1 = HP // ATK_Boss
if HP % ATK_Boss:
    turn1 += 1

if (HP_Boss - P) % ATK and (HP_Boss - P) % ATK + P <= ATK:
    turn2 = HP_Boss // ATK
    if HP_Boss % ATK:
        turn2 += 1

else:
    turn2 = (HP_Boss + S) // ATK
    if (HP_Boss + S) % ATK:
        turn2 += 1

if turn1 >= turn2:
    print('Victory!')
else:
    print('gg')
