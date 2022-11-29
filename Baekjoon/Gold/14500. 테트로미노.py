# https://www.acmicpc.net/problem/14500
import sys
sys.stdin = open('input.txt')

N, M = map(int, sys.stdin.readline().split())

paper = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

