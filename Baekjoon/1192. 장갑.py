'''
https://www.acmicpc.net/problem/1192

[문제]

어느 날 화학선생님이 화학시간에 맨날 딴짓만 하던 선영이에게 지하실에 가서 실험 때 쓸 장갑을 가져오라고 지시했다.
장갑엔 n가지 색상이 있고 지하실에는 2개의 통이 있는데 한쪽에는 n가지 색상의 왼손쪽 장갑이 들어있고 다른 한쪽에는 n가지 색상의 오른손쪽 장갑이 들어있다. 선영이는 각각의 통에 어떤 색깔의 장갑이 몇 개가 들어있는지 알고 있다.
그런데 지하실은 너무나도 깜깜해서 장갑을 꺼내도 색을 구별하기는 힘들고 양쪽의 통에서 임의로 장갑 여러개를 집어올 수 있다.
여러개의 장갑중에 항상 색깔이 같은 장갑의 쌍이 적어도 한 개이상 존재하도록 하기 위해서 선영이가 각각 통에서 가져와야할 장갑은 몇 개인지 구하라.

'''

n = int(input())
n_left = list(map(int,input().split()))
n_right = list(map(int,input().split()))
large_left = []
large_right = []

for i in range(n):
    if n_left[i] == 0 and n_right[i] != 0:
        large_right += [n_right[i]]
    elif n_right[i] == 0 and n_left[i] != 0:
        large_left += [n_left[i]]
    else:
        if n_left[i] > n_right[i]:
            large_right += [n_right[i]]
        else :
            large_left += [n_left[i]] 
            

if max(large_left) > max(large_right):
    answer_left = sum(large_left) - max(large_left) + 1
    answer_right = sum(large_right) + 1
else :
    answer_left = sum(large_left) + 1
    answer_right = sum(large_right)- max(large_right) + 1


print(answer_left)
print(answer_right)