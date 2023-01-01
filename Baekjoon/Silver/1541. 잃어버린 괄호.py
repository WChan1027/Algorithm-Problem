# https://www.acmicpc.net/problem/1541
import sys
sys.stdin = open('input.txt')

expression = sys.stdin.readline()

words = ''
num = 0
minus = False
for word in expression:
    if word == '-':
        if minus == False:
            minus = True
            num += int(words)
            words = ''
        else:
            num -= int(words)
            words = ''
    elif word == '+':
        if minus == False:
            num += int(words)
            words = ''
        else:
            num -= int(words)
            words = ''
    else:
        words += word

if minus == False:
    answer = num + int(words)
else:
    answer = num - int(words)

print(answer)