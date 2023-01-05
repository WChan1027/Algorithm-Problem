# https://www.acmicpc.net/problem/23762
import sys
# import itertools
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
skill = list(map(int, input().split()))

# com_skill = itertools.combinations(skill, N % 4)        # 혼자 치게 되는 사람의 조합
# skill_diff = max(skill) * N                             # 실력 차의 합
skill_sort = sorted(skill)

matrix = [[] for _ in range(4)]
idx = -1
length = 1

for i in range(N - 3):
    idx += 1
    if idx == 4:
        idx = 0
        length += 1

    value = skill_sort[i+3] - skill_sort[i]
    matrix[idx].append(value)

print(matrix)

answer = max(skill) * N
answer_idx = []

def check(result, n, m, change):            # change = [(n, m)]
    global length, answer, answer_idx
    if m == length:
        if result < answer:
            answer = result
            temp = []
            for i in change:
                temp.append()
            answer_idx = temp

    for i in range(m+1):
        if i != m:
            check(result + )


## 재귀 함수 사용

# alone_answer = []
#
# def check(com_skill, N):
#     global skill_diff, alone_answer
#     if len(com_skill) == N%4:
#         team = skill_sort[:]
#         result = 0
#         go = 1
#         for alone in com_skill:
#            team.remove(alone)
#
#         for i in range(0, len(team) - 3, 4):
#             result += team[i+3] - team[i]
#             if result > skill_diff:
#                 go = 0
#                 break
#
#         if go == 1 and result < skill_diff:
#             skill_diff = result
#             alone_answer = com_skill
#         return
#     else:
#         if com_skill:
#             a = skill.index(com_skill[-1])
#             for i in range(a+1, N-(N%4) + len(com_skill)):
#                 check(com_skill + [skill[i]], N)
#         else:
#             for i in range(N - (N%4)):
#                 check(com_skill + [skill[i]], N)
#         return
#
# arr = []
# check(arr, N)
#
# print(skill_diff)
# for i in alone_answer:
#     print(skill.index(i))


## combination 사용

# for no_team in com_skill:
#     team = skill_sort[:]
#     result = 0
#     go = 1
#     for alone in no_team:
#         team.remove(alone)
#
#     for i in range(0, len(team) - 3, 4):
#         result += team[i+3] - team[i]
#         if result > skill_diff:
#             go = 0
#             break
#
#     if go == 1 and result < skill_diff:
#         skill_diff = result
#         alone_answer = no_team
#
# print(skill_diff)
# for i in alone_answer:
#     print(skill.index(i))