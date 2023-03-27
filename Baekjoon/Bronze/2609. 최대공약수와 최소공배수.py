# https://www.acmicpc.net/problem/2609

A, B = map(int, input().split())

for i in range(min(A, B), 0, -1):
    if A % i == 0 and B % i == 0:
        divisor = i
        break

multiple = max(A, B)
while True:
    if multiple % A == 0 and multiple % B == 0:
        break
    multiple += 1

print(divisor)
print(multiple)