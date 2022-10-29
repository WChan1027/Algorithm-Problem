'''
https://www.acmicpc.net/problem/10814

[문제]

온라인 저지에 가입한 사람들의 나이와 이름이 가입한 순서대로 주어진다.
이때, 회원들을 나이가 증가하는 순으로, 나이가 같으면 먼저 가입한 사람이 앞에 오는 순서로 정렬하는 프로그램을 작성하시오.

'''

N = int(input())

member = [list(map(str, input().split())) for _ in range(N)]

for i in range(N):
    member[i][0] = int(member[i][0])

member.sort(key=lambda x:x[0])

for i in range(N):
    print(*member[i])