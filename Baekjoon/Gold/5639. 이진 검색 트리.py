# https://www.acmicpc.net/problem/5639
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

tree = []

root = int(input())
tree.append(root)

while True:
    try:
        node = int(input())
    except:
        break

    if node > tree[-1]:
        idx = len(tree) - 1
        while tree[idx] > node:
            idx -= 1
        while len(tree) > idx:
            print(tree.pop())

        print(node)

    else:
        tree.append(node)
