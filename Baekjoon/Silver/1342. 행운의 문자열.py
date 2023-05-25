import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

S = input()
answer = 0

# 팩토리얼 구하는 함수
def factorial(n):
    for i in range(2, n+1):
        factorial_memo[i-1] = factorial_memo[i-2] * i
    return

# 인접한 모든 문자가 같지 않은 문자열의 갯수를 구하는 함수
def lucky(word, last_word):
    global answer
    if not word:
        answer += 1
        return

    for i in word:
        if i != last_word:
            lucky(word.replace(f'{i}', '', 1), i)
    return

lucky(S, '1')

factorial_memo = [1] * len(S)

factorial(len(S))

# 중복 문자열 제거
for i in set(S):
    answer //= factorial_memo[S.count(i)-1]

print(answer)

#
# import sys
# sys.stdin = open('input.txt')
# from collections import Counter
#
#
# def backTracking(pre, l):
#     answer = 0
#
#     # 행운의 문자열이므로 1를 리턴
#     if l == len(s):
#         return 1
#
#     # 반복문을 통해 단어를 확인
#     for k in cnt.keys():
#         # 현재 단어가 이전 단어일 경우와 현재 단어의 개수가 0일 경우 다음 단어를 확인한다.
#         if k == pre or cnt[k] == 0:
#             continue
#
#         cnt[k] -= 1 # 현재 단어의 개수를 감소
#         answer += backTracking(k, l + 1) # 백트래킹 후 리턴 받은 수를 answer에 더한다.
#         cnt[k] += 1 # 현재 단어의 개수를 증가
#
#     # answer 리턴
#     return answer
#
#
# s = list(map(str, sys.stdin.readline().strip()))
# cnt = Counter(s) # 문자의 개수를 딕셔너리로 변환
# print(backTracking('', 0))