'''
https://www.acmicpc.net/problem/1978

[문제]

주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

'''

N = int(input())

num = list(map(int, input().split()))

prime_num = [2, 3]
for i in range(5, 1000):
    flag = 0
    for j in range(2, i//2):
        if i % j == 0:
            flag = 1
            break
    if flag == 0:
        prime_num.append(i)

answer = 0
for i in num:
    if i in prime_num:
        answer += 1

print(answer)