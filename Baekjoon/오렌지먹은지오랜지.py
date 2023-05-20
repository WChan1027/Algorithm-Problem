import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
sentence = input()

def is_orange(word1, word2, length):
    diff = 0
    for i in range(length):
        if word1[i] != word2[i]:
            diff += 1
            if diff > 1:
                return

    if diff == 1:
        return True

answer = 'NO'
for idx in range(1, N):
    if is_orange(sentence[:idx], sentence[N - idx:], idx):
        answer = 'YES'
        break

print(answer)