import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

word = input()

if 'M' in word and 'O' in word and 'B' in word and 'I' in word and 'S' in word:
    print('YES')
else:
    print('NO')