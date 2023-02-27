# https://www.acmicpc.net/contest/problem/956/4
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

Q = int(input())

count = dict()
sum = 0

for test_case in range(Q):
    query = input().strip()
    num = int(query[1:])

    if query[0] == '+':
        sum += num
        a = sum
        answer = 0
        while a // 2 > 0:
            answer += 1
            a //= 2

        print(2**answer)

    else:
        sum -= num

        a = sum
        answer = 0
        while a // 2 > 0:
            answer += 1
            a //= 2

        if sum == 0:
            print(0)
        else:
            print(2**answer)

    #
    # count = dict(sorted(count.items()))
    #
    # if query[0] == '+':
    #     if num in count.keys():
    #         count[num] += 1
    #         if num != 0:
    #             if count[num] == 2:
    #                 count[num] = 1
    #                 while count[num] == 1:
    #                     del count[num]
    #                     num *= 2
    #                     if num not in count.keys():
    #                         count[num] = 0
    #                 count[num] = 1
    #
    #     else:
    #         count[num] = 1
    #
    #     keys = list(count.keys())
    #     print(count)
    #     # print(keys[-1])
    #
    # else:
    #     if num in count.keys():
    #         count[num] -= 1
    #     else:
    #         count[num] = -1
    #
    #     if count[num] < 0:
    #         count[num] = 1
    #         num *= 2
    #         while num not in count.keys():
    #             count[num] = 1
    #             num *= 2
    #
    #         del count[num]
    #     print(count)
    #     keys = list(count.keys())
    #
    #     if count:
    #         while count[keys[-1]] == 0:
    #             del count[keys[-1]]
    #             keys.pop()
    #             if not count:
    #                 break
    #         if count:
    #             print(keys[-1])
    #         else:
    #             print(0)
    #     else:
    #         print(0)