import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

T, W = map(int, input().split())

tree = list(int(input()) for _ in range(T))

