# https://www.acmicpc.net/problem/14653
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, K, Q = map(int, input().split())

name = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
name = name[:N]
name.remove('A')
messages = [list(map(str, input().split())) for _ in range(K)]

if int(messages[Q-1][0]) == 0:
    print(-1)
else:
    for message in messages:
        if int(message[0]) >= int(messages[Q-1][0]):
            if message[1] in name:
                name.remove(message[1])

    print(*name)