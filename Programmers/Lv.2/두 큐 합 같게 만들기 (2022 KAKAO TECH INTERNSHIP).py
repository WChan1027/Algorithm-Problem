from collections import deque

def solution(queue1, queue2):
    all_elements = queue1 + queue2
    if sum(all_elements) % 2:
        return -1

    queue1, queue2 = deque(queue1), deque(queue2)
    cnt = 0
    q1, q2 = sum(queue1), sum(queue2)

    while True:
        if q1 > q2:
            n = queue1.popleft()
            queue2.append(n)
            q1, q2 = q1 - n, q2 + n
        elif q1 < q2:
            n = queue2.popleft()
            queue1.append(n)
            q1, q2 = q1 + n, q2 - n
        else:
            return cnt

        cnt += 1
        if cnt == len(all_elements) * 2:
            return -1