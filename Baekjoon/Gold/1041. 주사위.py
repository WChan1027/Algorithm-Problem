'''
https://www.acmicpc.net/problem/1041

[문제]

주사위는 위와 같이 생겼다. 주사위의 여섯 면에는 수가 쓰여 있다.
위의 전개도를 수가 밖으로 나오게 접는다.
A, B, C, D, E, F에 쓰여 있는 수가 주어진다.
지민이는 현재 동일한 주사위를 N^3개 가지고 있다.
이 주사위를 적절히 회전시키고 쌓아서, N×N×N크기의 정육면체를 만들려고 한다.
이 정육면체는 탁자위에 있으므로, 5개의 면만 보인다.
N과 주사위에 쓰여 있는 수가 주어질 때, 보이는 5개의 면에 쓰여 있는 수의 합의 최솟값을 출력하는 프로그램을 작성하시오.

'''

N = int(input())
A, B, C, D, E, F = map(int, input().split())
num = [A, B, C, D, E, F]

sum_two_num = []
sum_three_num = []
for i in range(len(num)-1):
    for j in range(i+1, len(num)):
        if i == 0 and j == 5:
            pass
        elif i == 1 and j == 4:
            pass
        elif i == 2 and j == 3:
            pass
        else:
            sum_two_num.append(num[i] + num[j])

for i in range(len(num)-2):
    for j in range(i+1, len(num)-1):
        for k in range(j+1, len(num)):
            if 0 in [i, j, k] and 5 in [i, j, k]:
                pass
            elif 1 in [i, j, k] and 4 in [i, j, k]:
                pass
            elif 2 in [i, j, k] and 3 in [i, j, k]:
                pass
            else:
                sum_three_num.append(num[i] + num[j] + num[k])

sum_num = ((N-1)*4 + (N-2)*4)*(min(sum_two_num)) + ((N-1)*(N-2)*4 + (N-2)*(N-2))*(min(num)) + 4*(min(sum_three_num))

if N == 1:
    sum_num = sum(num) - max(num)
elif N == 2:
    sum_num = 4*(min(sum_two_num) + min(sum_three_num))
print(sum_num)