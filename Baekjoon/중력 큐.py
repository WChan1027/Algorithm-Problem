import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline

Q = int(input())

que = deque()
rotate = 0
b = 0
w = 0
for case in range(Q):
    order = list(map(str, input().split()))
    if order[0] == 'push':
        if order[1] == 'b':
            if rotate == 0 or rotate == 180:
                que.append('b')
                b += 1

            elif rotate == 90:
                if w > 0:
                    que.append('b')
                    b += 1

        elif order[1] == 'w':
            que.append('w')
            w += 1

    elif order[0] == 'pop':
        if que:
            a = que.popleft()
            if a == 'b':
                b -= 1
            else:
                w -= 1

    elif order[0] == 'rotate':
        if order[1] == 'l':
            rotate -= 90
            rotate %= 360
            if rotate == 90:
                if w == 0:
                    que = deque()
                    b = 0
                while que:
                    if que[0] == 'b':
                        que.popleft()
                        b -= 1
                    else:
                        break

            if rotate == 270:
                if w == 0:
                    que = deque()
                    b = 0
                while que:
                    if que[-1] == 'b':
                        que.pop()
                        b -= 1
                    else:
                        break

        elif order[1] == 'r':
            rotate += 90
            rotate %= 360
            if rotate == 90:
                if w == 0:
                    que = deque()
                    b = 0
                while que:
                    if que[0] == 'b':
                        que.popleft()
                        b -= 1
                    else:
                        break

            if rotate == 270:
                if w == 0:
                    que = deque()
                    b = 0
                while que:
                    if que[-1] == 'b':
                        que.pop()
                        b -= 1
                    else:
                        break

    elif order[0] == 'count':
        if order[1] == 'b':
            print(b)

        elif order[1] == 'w':
            print(w)