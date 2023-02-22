# https://www.acmicpc.net/problem/9935
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

word = input().strip()
bomb = input().strip()

answer = []
for string in word:
    answer.append(string)
    if string == bomb[-1]:
        if ''.join(answer[-len(bomb):]) == bomb:
            for _ in range(len(bomb)):
                answer.pop()

if answer:
    print(''.join(answer))
else:
    print('FRULA')