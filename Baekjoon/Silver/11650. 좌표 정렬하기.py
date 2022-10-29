'''
https://www.acmicpc.net/problem/11650

[문제]

2차원 평면 위의 점 N개가 주어진다.
좌표를 x좌표가 증가하는 순으로, x좌표가 같으면 y좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.

'''

N = int(input())
location = []

for _ in range(N):
    location.append(list(map(int, input().split())))

location.sort(key = lambda x:x[1])
location.sort(key = lambda x:x[0])

for i in location:
    print(*i)