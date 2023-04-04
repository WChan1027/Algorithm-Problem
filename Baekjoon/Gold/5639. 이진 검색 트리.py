# https://www.acmicpc.net/problem/5639
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

tree = []
tree_right = []

root = int(input())
tree.append(root)

while True:
    try:
        node = int(input())
    except:
        break

    if node > root:
        tree_right.append(node)
        break

    if node > tree[-1]:
        idx = len(tree) - 1
        while tree[idx] > node:
            idx -= 1
        print(idx, tree[idx])
        while len(tree) > idx:
            print(tree.pop())

        print(node)

    else:
        tree.append(node)

    print(tree)

print(tree.pop())

while True:
    try:
        node = int(input())
    except:
        break

    if node > tree_right[-1]:
        idx = len(tree_right) - 1
        while tree_right[idx] > node:
            idx -= 1
        while len(tree_right) > idx:
            print(tree_right.pop())

        print(node)

    else:
        tree_right.append(node)

print(tree_right.pop())
print(tree.pop())