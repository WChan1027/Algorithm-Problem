import sys
from itertools import product
sys.stdin = open('input.txt')
input = sys.stdin.readline

father = list(map(str, input().strip().split()))
mother = list(map(str, input().strip().split()))
color = set(father + mother)
child = list(product(color, repeat=2))
child.sort()

for colors in child:
    print(*colors)
