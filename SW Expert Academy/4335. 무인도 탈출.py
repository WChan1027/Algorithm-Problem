# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWL6HGz6Ai4DFAUY
import sys
sys.stdin = open('input.txt')

def stack(box, height):




T = int(sys.stdin.readline())

for test_case in range(1, T+1):
    N = int(sys.stdin.readline())
    boxes = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

