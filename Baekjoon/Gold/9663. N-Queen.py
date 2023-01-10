# https://www.acmicpc.net/problem/9663
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())

chess = [[0] * N for _ in range(N)]

def check()