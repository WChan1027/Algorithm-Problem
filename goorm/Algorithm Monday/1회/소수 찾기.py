'''
문제

정수로 이루어진 수열 A에 있는 수들을 합한 값을 구하기로 한다.
하지만 평범한 합하기는 너무 쉽게 구해지기 때문에, 새로운 조건을 추가하여 값을 추출하고, 추출된 모든 값을 합하기로 한다.
새로운 조건은 아래와 같다.

- 수열 A의 i번째 수를 Ai라고 부른다.
- i가 소수인 Ai를 추출한다.

조건에 따라서 추출된 값들을 모두 합하고, 그 값을 출력하시오.

'''

n = int(input())

A = list(map(int, input().split()))

A.insert(0, 0)

prime_number = [0] * (n+1)
prime_number[2] = 1
prime_number[3] = 1
if n > 4:
    for i in range(5, n+1):
        prime = 1
        for j in range(2, i//2 + 1):
            if i % j == 0:
                prime = 0
                break
        if prime == 1:
            prime_number[i] = 1
    answer = 0
    for i in range(n+1):
        if prime_number[i] == 1:
            answer += A[i]
elif n == 1:
    answer = 0
elif n == 2:
    answer = A[2]
elif n <= 4:
    answer = A[2] + A[3]

print(answer)