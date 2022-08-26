'''
https://www.acmicpc.net/problem/2628

[문제]

직사각형 모양의 종이가 있다.
이 종이는 가로방향과 세로 방향으로 1㎝마다 점선이 그어져 있다.
점선은 위에서 아래로 1번부터 차례로 번호가 붙어 있고, 세로 점선은 왼쪽에서 오른쪽으로 번호가 붙어 있다.
점선을 따라 이 종이를 칼로 자르려고 한다.
가로 점선을 따라 자르는 경우는 종이의 왼쪽 끝에서 오른쪽 끝까지, 세로 점선인 경우는 위쪽 끝에서 아래쪽 끝까지 한 번에 자른다.
입력으로 종이의 가로 세로 길이, 그리고 잘라야할 점선들이 주어질 때, 가장 큰 종이 조각의 넓이가 몇 ㎠인지를 구하는 프로그램을 작성하시오.

'''

length, height = map(int, input().split())

N = int(input())
cut_length = [0, length]
cut_height = [0, height]
max_length = 0
max_height = 0

for _ in range(N):
    dotted_line = list(map(int, input().split()))
    if dotted_line[0] == 1:
        cut_length.append(dotted_line[1])
    else:
        cut_height.append(dotted_line[1])

for i in range(len(cut_length)-1):
    for j in range(len(cut_length)-1, i, -1):
        if cut_length[j] < cut_length[j-1]:
            cut_length[j], cut_length[j-1] = cut_length[j-1], cut_length[j]

for i in range(len(cut_height)-1):
    for j in range(len(cut_height)-1, i, -1):
        if cut_height[j] < cut_height[j-1]:
            cut_height[j], cut_height[j-1] = cut_height[j-1], cut_height[j]

for i in range(len(cut_length)-1):
    if cut_length[i+1] - cut_length[i] > max_length:
        max_length = cut_length[i+1] - cut_length[i]

for i in range(len(cut_height)-1):
    if cut_height[i+1] - cut_height[i] > max_height:
        max_height = cut_height[i+1] - cut_height[i]

answer = max_length * max_height

print(answer)