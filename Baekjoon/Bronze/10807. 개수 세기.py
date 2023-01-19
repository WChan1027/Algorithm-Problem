# https://www.acmicpc.net/problem/10807
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())

num = list(map(int, input().split()))

v = int(input())

print(num.count(v))