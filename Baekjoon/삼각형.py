import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

W, H = map(int, input().split())

area = (W * H) / 2
answer = '{:.1f}'.format(area)

print(answer)