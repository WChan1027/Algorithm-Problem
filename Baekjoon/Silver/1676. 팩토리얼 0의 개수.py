'''
https://www.acmicpc.net/problem/1676

[문제]

N!에서 뒤에서부터 처음 0이 아닌 숫자가 나올 때까지 0의 개수를 구하는 프로그램을 작성하시오.

'''

N = int(input())

print(N//5 + N//25 + N//125)