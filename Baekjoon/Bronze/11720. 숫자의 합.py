'''
https://www.acmicpc.net/problem/11720

[문제]

N개의 숫자가 공백 없이 쓰여있다. 이 숫자를 모두 합해서 출력하는 프로그램을 작성하시오.

'''

N = int(input())
num = str(input())
answer = 0

for i in num:
    answer += int(i)

print(answer)