import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
word = input()

def orange(word):
    for i in range(1, N):
        if word[0] == word[i]:
            check = 0
            end = 0
            for k in range(1, N - i):
                if word[k] != word[i+k]:
                    if check == 0:
                        check = 1
                    else:
                        break
                if k == N-i-1:
                    end = 1
            if check == 1 and end == 1:
                return 1

    return 0

if orange(word) == 1:
    print('YES')
else:
    print('NO')