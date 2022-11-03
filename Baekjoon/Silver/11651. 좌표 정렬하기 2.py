'''
https://www.acmicpc.net/problem/11651

[문제]

2차원 평면 위의 점 N개가 주어진다.
좌표를 y좌표가 증가하는 순으로, y좌표가 같으면 x좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.

'''

N = int(input())

coordinate = [list(map(int, input().split())) for _ in range(N)]

coordinate.sort()
coordinate.sort(key=lambda x:x[1])

for i in coordinate:
    print(*i)