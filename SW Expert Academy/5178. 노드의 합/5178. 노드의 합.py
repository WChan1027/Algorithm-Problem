import sys
sys.stdin = open('sample_input.txt')

def make_tree(node):
    if node:
        make_tree(tree[node][0])
        make_tree(tree[node][1])
        if tree[node][0] != 0:
            tree[node][3] = tree[tree[node][0]][3] + tree[tree[node][1]][3]


T = int(input())

for test_case in range(1, T+1):
    N, M, L = map(int, input().split())

    tree = [[0, 0, 0, 0] for _ in range(N+1)]

    for _ in range(M):
        leaf_node, num = map(int, input().split())
        tree[leaf_node][3] = num

    for i in range(1, N+1):
        if i*2 <= N:
            tree[i][0] = i*2
        if i*2 + 1 <= N:
            tree[i][1] = i*2 + 1
        tree[i][2] = i//2

    make_tree(1)
    answer = tree[L][3]

    print(f'#{test_case} {answer}')