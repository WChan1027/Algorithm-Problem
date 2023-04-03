import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

c, h = map(int, input().split())

seconds = [0] * 24*60*60

for _ in range(c):
    time = list(map(int, input().split(':')))
    start = time[0] * 60 * 60 + time[1] * 60 + time[2]

    seconds[start:start+40] = [1] * 40

for _ in range(h):
    time = list(map(int, input().split(':')))
    start = time[0] * 60 * 60 + time[1] * 60 + time[2]

    seconds[start:start + 40] = [1] * 40

print(seconds.count(0))