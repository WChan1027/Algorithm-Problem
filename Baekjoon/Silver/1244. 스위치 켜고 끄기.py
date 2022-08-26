'''
https://www.acmicpc.net/problem/1244

[문제]

1부터 연속적으로 번호가 붙어있는 스위치들이 있다.
스위치는 켜져 있거나 꺼져있는 상태이다.
‘1’은 스위치가 켜져 있음을, ‘0’은 꺼져 있음을 나타낸다.
그리고 학생 몇 명을 뽑아서, 학생들에게 1 이상이고 스위치 개수 이하인 자연수를 하나씩 나누어주었다.
학생들은 자신의 성별과 받은 수에 따라 아래와 같은 방식으로 스위치를 조작하게 된다.

남학생은 스위치 번호가 자기가 받은 수의 배수이면, 그 스위치의 상태를 바꾼다.
즉, 스위치가 켜져 있으면 끄고, 꺼져 있으면 켠다.

여학생은 자기가 받은 수와 같은 번호가 붙은 스위치를 중심으로 좌우가 대칭이면서 가장 많은 스위치를 포함하는 구간을 찾아서, 그 구간에 속한 스위치의 상태를 모두 바꾼다.
이때 구간에 속한 스위치 개수는 항상 홀수가 된다.

입력으로 스위치들의 처음 상태가 주어지고, 각 학생의 성별과 받은 수가 주어진다.
학생들은 입력되는 순서대로 자기의 성별과 받은 수에 따라 스위치의 상태를 바꾸었을 때, 스위치들의 마지막 상태를 출력하는 프로그램을 작성하시오.

'''

N = int(input())
initial = list(map(int, input().split()))

num_students = int(input())

for i in range(num_students):
    student = list(map(int, input().split()))
    if student[0] == 1:
        for j in range(N // student[1]):
            if initial[(j+1)*student[1]-1] == 0:
                initial[(j+1)*student[1]-1] = 1
            else:
                initial[(j+1)*student[1]-1] = 0
    else:
        if initial[student[1] - 1] == 0:
            initial[student[1] - 1] = 1
        else:
            initial[student[1] - 1] = 0
        n = 0
        while True:
            n += 1
            if student[1] - 1 - n < 0 or student[1] - 1 + n >= N:
                break
            if initial[student[1] - 1 - n] == initial[student[1] - 1 + n]:
                if initial[student[1] - 1 - n] == 0:
                    initial[student[1] - 1 - n] = 1
                    initial[student[1] - 1 + n] = 1
                else:
                    initial[student[1] - 1 - n] = 0
                    initial[student[1] - 1 + n] = 0
            else:
                break


n = 0
for i in range(len(initial)):
    n += 1
    if n % 20 == 0:
        print(initial[i])
    else:
        print(initial[i], end=' ')
