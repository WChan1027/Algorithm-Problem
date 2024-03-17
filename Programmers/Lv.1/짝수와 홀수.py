'''
https://school.programmers.co.kr/learn/courses/30/lessons/12937

[문제]

정수 num이 짝수일 경우 "Even"을 반환하고 홀수인 경우 "Odd"를 반환하는 함수, solution을 완성해주세요.


[제한사항]

- num은 int 범위의 정수입니다.
- 0은 짝수입니다.

'''

def solution(num):
    return 'Even' if num % 2 == 0 else 'Odd'