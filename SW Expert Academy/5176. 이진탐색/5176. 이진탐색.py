import sys
sys.stdin = open('sample_input.txt')

# 중위 순회의 순서대로 숫자 부여
def set(node):
    global n
    if node:
        set(tree[node][0])
        tree[node][3] = n
        n += 1
        set(tree[node][1])


T = int(input())

for test_case in range(1, T+1):
    N = int(input())

    tree = [[0, 0, 0, 0] for _ in range(N+1)]

    for i in range(1, N+1):
        if i*2 <= N:
            tree[i][0] = i*2
        if i*2 + 1 <= N:
            tree[i][1] = i*2 + 1
        tree[i][2] = i//2

    n = 1
    set(1)

    print(f'#{test_case} {tree[1][3]} {tree[N//2][3]}')