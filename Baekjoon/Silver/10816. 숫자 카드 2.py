'''
https://www.acmicpc.net/problem/10816

[문제]

숫자 카드는 정수 하나가 적혀져 있는 카드이다. 상근이는 숫자 카드 N개를 가지고 있다.
정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 상근이가 몇 개 가지고 있는지 구하는 프로그램을 작성하시오.

'''
import sys
N = int(sys.stdin.readline())

card = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())

num = list(map(int, sys.stdin.readline().split()))

card_dict = {}
for i in card:
    if i in card_dict:
        card_dict[i] += 1
    else:
        card_dict[i] = 1

for i in num:
    if i in card_dict:
        print(card_dict[i], end=' ')
    else:
        print(0, end=' ')