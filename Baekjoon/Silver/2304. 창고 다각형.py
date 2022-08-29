'''
https://www.acmicpc.net/problem/2304

[문제]

N 개의 막대 기둥이 일렬로 세워져 있다. 기둥들의 폭은 모두 1 m이며 높이는 다를 수 있다.
이 기둥들을 이용하여 양철로 된 창고를 제작하려고 한다.
창고에는 모든 기둥이 들어간다. 이 창고의 지붕을 다음과 같이 만든다.

1. 지붕은 수평 부분과 수직 부분으로 구성되며, 모두 연결되어야 한다.
2. 지붕의 수평 부분은 반드시 어떤 기둥의 윗면과 닿아야 한다.
3. 지붕의 수직 부분은 반드시 어떤 기둥의 옆면과 닿아야 한다.
4. 지붕의 가장자리는 땅에 닿아야 한다.
5. 비가 올 때 물이 고이지 않도록 지붕의 어떤 부분도 오목하게 들어간 부분이 없어야 한다.

창고 주인은 창고 다각형의 면적이 가장 작은 창고를 만들기를 원한다.
기둥들의 위치와 높이가 주어질 때, 가장 작은 창고 다각형의 면적을 구하는 프로그램을 작성하시오.

'''

def long_right(a, N):
    if a == N-1:
        return
    tall = 0
    for i in range(a+1, N):
        if column[i][1] > tall:
            tall = column[i][1]
            tall_locate_right = i
    roof.append(tall_locate_right)
    long_right(tall_locate_right, N)
    return

def long_left(a, N):
    if a == 0:
        return
    tall = 0
    for i in range(a):
        if column[i][1] > tall:
            tall = column[i][1]
            tall_locate_left = i
    roof.append(tall_locate_left)
    long_left(tall_locate_left, N)
    return

N = int(input())

column = []
roof = []

for i in range(N):
    column += [list(map(int, input().split()))]

column.sort()

tallest = 0

for i in range(N):
    if column[i][1] > tallest:
        tallest = column[i][1]
        tallest_locate = i

roof.append(tallest_locate)

long_right(tallest_locate, N)
long_left(tallest_locate, N)

answer = 0

roof.sort()

for i in range(len(roof)):
    if roof[i] < tallest_locate:
        answer += (column[roof[i+1]][0] - column[roof[i]][0]) * column[roof[i]][1]
    elif roof[i] > tallest_locate:
        answer += (column[roof[i]][0] - column[roof[i-1]][0]) * column[roof[i]][1]
    else:
        answer += column[tallest_locate][1]

print(answer)