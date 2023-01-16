# https://www.acmicpc.net/problem/1629
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

A, B, C = map(int, input().split())

remain = [1, A % C]
result = A
n = 1
while B > 0:
    N = 2 ** (n - 1)
    if B < N:
        n -= 1

    elif B == N:
        result = (result * remain[n-1]) % C
        B = 0

    else:
        B -= N
        n += 1
        result = (result * remain[n-1]) % C
        if n == len(remain):
            remain.append(result)

print(result)

# remain = []
# a = []
# result = 1
# for i in range(B):
#     result *= A
#     if result >= C:
#         result %= C
#     if result in remain:
#         a = remain[remain.index(result):]
#     else:
#         remain.append(result)
#
# if a:
#     print(a[(B - len(remain) - len(a) - 1)%len(a)])
# else:
#     print(result)



# remain = []
#
# def cal(result):
#     result = (result * A) % C
#     if result in remain:
#         a = remain.index(result)
#         return remain[a:]
#     else:
#         remain.append(result)
#         return cal(result)
#
# c = cal(1)
#
# b = B - (len(remain) - len(c)) - 1
# print(c[b%len(c)])



# answer = 1
# for i in range(B):
#     answer *= A
#     answer %= C
#
# print(answer)