import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

answer = 0
while True:
    try:
        way = list(map(str, input().split()))
        if way[0] == 'Es':
            answer += int(way[1]) * 21
        else:
            answer += int(way[1]) * 17
    except:
        break

print(answer)