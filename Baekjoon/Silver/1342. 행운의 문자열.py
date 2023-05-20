import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

S = input()
answer = 0

def check(word, last):
    global answer
    # if not word:
    #     answer += 1
    #     return

    for str in word:
        if str != last:
            new_word = word.replace(str, "", 1)
            if not new_word:
                answer += 1
                return
            check(new_word, str)
    else:
        return

check(S, 0)
print(answer)