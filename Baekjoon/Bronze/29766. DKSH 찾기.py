import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

sentence = input().strip()

print(sentence.count('DKSH'))