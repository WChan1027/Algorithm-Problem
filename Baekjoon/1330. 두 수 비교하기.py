'''
https://www.acmicpc.net/problem/1001

[문제]

두 정수 A와 B를 입력받은 다음, A-B를 출력하는 프로그램을 작성하시오.

'''

A, B = map(int, input().split())

if A > B:
    print('>')
elif A < B:
    print('<')
else:
    print('==')