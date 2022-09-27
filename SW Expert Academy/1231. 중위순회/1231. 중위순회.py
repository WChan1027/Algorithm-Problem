import sys
sys.stdin = open('input.txt')

def in_order(node):
    node = int(node)
    if node:
        in_order(data[node][2])
        print(data[node][1], end='')
        in_order(data[node][3])


for test_case in range(1, 11):
    N = int(input())
    data = [input().split() for _ in range(N)]
    data.insert(0, [0, 0, 0, 0])
    for i in data:
        while len(i) != 4:
            i.append(0)
    print(f'#{test_case}', end=' ')
    in_order(data[1][0])
    print()