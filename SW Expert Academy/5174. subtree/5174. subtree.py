import sys
sys.stdin = open('sample_input.txt')

def num_of_node(node):
    global answer
    if node:
        answer += 1
        num_of_node(tree[node][0])
        num_of_node(tree[node][1])


T = int(input())

for test_case in range(1, T+1):
    E, N = map(int, input().split())

    arr = list(map(int, input().split()))

    tree = [[0, 0, 0]]

    for i in range(E):
        parent, child = arr[i*2], arr[i*2 + 1]
        while len(tree) <= parent:
            tree.append([0, 0, 0])
        if tree[parent][0] == 0:
            tree[parent][0] = child
        else:
            tree[parent][1] = child
        while len(tree) <= child:
            tree.append([0, 0, 0])
        tree[child][2] = parent

    answer = 0
    num_of_node(N)

    print(f'#{test_case} {answer}')