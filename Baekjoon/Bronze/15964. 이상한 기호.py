# https://www.acmicpc.net/problem/15964
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

A, B = map(int, input().split())

print((A+B)*(A-B))