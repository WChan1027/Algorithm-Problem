# https://www.acmicpc.net/problem/2480
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

dices = list(map(int, input().split()))

reward = 0
for dice in dices:
    if dices.count(dice) == 3:
        reward = 10000 + 1000 * dice
        break
    elif dices.count(dice) == 2:
        reward = 1000 + 100 * dice
        break
    else:
        if reward < 100 * dice:
            reward = 100 * dice

print(reward)