import sys
from collections import defaultdict
sys.stdin = open('input.txt')
input = sys.stdin.readline

S = input()
answer = 0

def lucky(word, last_word):
    global answer
    if not word:
        answer += 1
        return

    for i in word:
        if i != last_word:
            word = word.replace(f'{i}', '', 1)
            lucky(word, i)
            word += f'{i}'
    return

EA = defaultdict(int)
for i in S:
    EA[i] += 1

factorial = [1] * (len(S)//2)
for i in range(1, len(S)//2 + 1):
    factorial[i] = factorial[i-1] * i

lucky(S, '0')

for i in EA.values():
    if i > 1:
        answer //= factorial(i)

print(answer)