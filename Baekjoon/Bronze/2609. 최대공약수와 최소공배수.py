'''
https://www.acmicpc.net/problem/2609

[문제]

두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.

'''

A, B = map(int, input().split())

for i in range(min(A, B), 0, -1):
    if A % i == 0 and B % i == 0:
        divisor = i
        break

multiple = max(A, B)
while True:
    if multiple % A == 0 and multiple % B == 0:
        break
    multiple += 1

print(divisor)
print(multiple)