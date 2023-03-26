# https://www.acmicpc.net/problem/1918
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

equation = input().strip()

stack = []
result = ''

for word in equation:
    if word.isalpha():
        result += word
    else:
        if word == '(':
            stack.append(word)
        elif word == '*' or word == '/':
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                result += stack.pop()
            stack.append(word)
        elif word == '+' or word == '-':
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.append(word)
        elif word == ')':
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.pop()

while stack:
    result += stack.pop()

print(result)