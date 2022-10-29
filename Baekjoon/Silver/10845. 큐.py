'''
https://www.acmicpc.net/problem/10845

[문제]

정수를 저장하는 큐를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

명령은 총 여섯 가지이다.

    - push X: 정수 X를 큐에 넣는 연산이다.
    - pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    - size: 큐에 들어있는 정수의 개수를 출력한다.
    - empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
    - front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    - back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.

'''
from collections import deque
N = int(input())

queue = deque()
answer = deque()
for test_case in range(N):
    order = list(map(str, input().split()))
    if order[0] == 'push':
        queue.append(int(order[1]))
    elif order[0] == 'pop':
        if queue:
            answer.append(queue.popleft())
        else:
            answer.append(-1)
    elif order[0] == 'size':
        answer.append(len(queue))
    elif order[0] == 'empty':
        if queue:
            answer.append(0)
        else:
            answer.append(1)
    elif order[0] == 'front':
        if queue:
            answer.append(queue[0])
        else:
            answer.append(-1)
    elif order[0] == 'back':
        if queue:
            answer.append(queue[-1])
        else:
            answer.append(-1)

for i in answer:
    print(i)