'''
https://www.acmicpc.net/problem/2744

[문제]

영어 소문자와 대문자로 이루어진 단어를 입력받은 뒤, 대문자는 소문자로, 소문자는 대문자로 바꾸어 출력하는 프로그램을 작성하시오.

'''

word = input()
answer = ''

for i in word:
    if i.isupper():
        answer += i.lower()
    else:
        answer += i.upper()

print(answer)