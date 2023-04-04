import sys
from collections import defaultdict
sys.stdin = open('input.txt')
input = sys.stdin.readline

n, k = map(int, input().split())

students = list(map(int, input().split()))

if n == 1:
    print(0)
else:
    diff = defaultdict(int)
    diff[abs(students[0] - students[1])] += 1
    diff[abs(students[n-2] - students[n-1])] += 1

    for i in range(1, n-1):
        diff[max(abs(students[i] - students[i+1]), abs(students[i] - students[i-1]))] += 1

    flag = 0
    keys = list(diff.keys())
    keys.sort(reverse=True)
    if k == n:
        flag = 1
        print(0)
    else:
        if diff[keys[0]] > k:
            flag = 1
            print(keys[0])
        else:
            k -= diff[keys[0]]
            for i in range(1, len(keys)):
                if k >= diff[keys[i]]:
                    k -= diff[keys[i]]
                else:
                    print(keys[i])
                    flag = 1
                    break
    if flag == 0:
        print(0)