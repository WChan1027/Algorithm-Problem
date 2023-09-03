# https://www.acmicpc.net/problem/1099
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

sentence = input().strip()
N = int(input())

words = [input().strip() for _ in range(N)]


def check_word(word1, word2):
    A = list(word1)
    B = list(word2)
    A.sort()
    B.sort()

    return True if A == B else False

def check_value(word1, word2):
    result = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            result += 1

    return result

cnt = [float('inf')] * (len(sentence)+1)
cnt[0] = 0

for i in range(1, len(sentence) + 1):
    for word in words:
        if i >= len(word) and check_word(sentence[i - len(word):i], word):
            cnt[i] = min(cnt[i], cnt[i - len(word)] + check_value(sentence[i - len(word):i], word))

print(cnt[-1]) if cnt[-1] != float('inf') else print(-1)