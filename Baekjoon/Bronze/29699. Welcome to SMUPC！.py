import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())

sentence = 'WelcomeToSMUPC'

print(sentence[N % len(sentence) - 1])