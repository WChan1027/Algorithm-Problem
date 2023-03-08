import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

word1 = input().strip()
word2 = input().strip()

cnt = [0] * max(len(word1), len(word2))

for i in range(len(word1)):
    result = 0
    for j in range(len(word2)):
        if result < cnt[j]:
            result = cnt[j]
        elif word1[i] == word2[j]:
            cnt[j] = max(cnt[j], result + 1)

print(max(cnt))