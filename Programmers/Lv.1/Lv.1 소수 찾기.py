'''
https://school.programmers.co.kr/learn/courses/30/lessons/12921

[문제]

1부터 입력받은 숫자 n 사이에 있는 소수의 개수를 반환하는 함수, solution을 만들어 보세요.


[제한사항]

- n은 2이상 1000000이하의 자연수입니다.

'''

def solution(n):
    number = list(range(n+1))
    not_prime_number = []
    for i in range(2, n+1):
        not_prime_number += number[2*i:n+1:i]

    answer = n - len(set(not_prime_number)) - 1

    return answer