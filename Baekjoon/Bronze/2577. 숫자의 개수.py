# https://www.acmicpc.net/problem/2577

num = 1
for _ in range(3):
    num *= int(input())

for i in range(10):
    print(str(num).count(str(i)))