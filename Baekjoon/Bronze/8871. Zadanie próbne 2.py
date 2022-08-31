'''
https://www.acmicpc.net/problem/8871

[문제]

Wyobraźmy sobie przez chwilę, że w tym roku konkurs SKI'10 składa się z n punktowanych rund i jednej rundy próbnej.
Ile zgodnie z regulaminem może się pojawić zadań w czasie całych zawodów?

'''

n = int(input())

print((n+1)*2, (n+1)*3)