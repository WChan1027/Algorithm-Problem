'''
https://www.acmicpc.net/problem/2108

[문제]

수를 처리하는 것은 통계학에서 상당히 중요한 일이다.
통계학에서 N개의 수를 대표하는 기본 통계값에는 다음과 같은 것들이 있다.
단, N은 홀수라고 가정하자.

    1. 산술평균 : N개의 수들의 합을 N으로 나눈 값
    2. 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
    3. 최빈값 : N개의 수들 중 가장 많이 나타나는 값
    4. 범위 : N개의 수들 중 최댓값과 최솟값의 차이

N개의 수가 주어졌을 때, 네 가지 기본 통계값을 구하는 프로그램을 작성하시오.

'''
import sys
N = int(sys.stdin.readline())

num = []
for _ in range(N):
    num.append(int(sys.stdin.readline()))

print(round(sum(num) / len(num)))
num.sort()
print(num[len(num)//2])
EA = {}
for i in num:
    if i in EA:
        EA[i] += 1
    else:
        EA[i] = 1
candi = []
a = max(EA.values())
for i in num:
    if EA[i] == a:
        candi.append(i)
if len(set(candi)) == 1:
    print(candi[0])
else:
    candi = list(set(candi))
    candi.sort()
    print(candi[1])

print(num[-1] - num[0])