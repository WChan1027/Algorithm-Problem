import sys
sys.stdin = open('input.txt')


for test_case in range(1, 11):
    N, S = map(int, input().split())
    contact = list(map(int, input().split()))

    order = dict(enumerate(sorted(list(set(contact)))))
    order_kv_reverse = {v:k for k, v in order.items()}
    start_point = order_kv_reverse[S]

    tree = [[0]*len(order) for _ in range(len(order))]
    visited = [0] * len(order)

    for i in range(N//2):
        tree[order_kv_reverse[contact[2*i]]][order_kv_reverse[contact[2*i + 1]]] = 1

    now = start_point
    stack = [now]
    visited[now] = 1
    while stack:
        now = stack.pop(0)
        for next in range(len(order)):
            if visited[next] == 0 and tree[now][next] == 1:
                stack.append(next)
                visited[next] = visited[now] + 1
    visited[start_point] = 1

    for i in range(len(order)-1, -1, -1):
        if visited[i] == max(visited):
            answer = order[i]
            break

    print(f'#{test_case} {answer}')