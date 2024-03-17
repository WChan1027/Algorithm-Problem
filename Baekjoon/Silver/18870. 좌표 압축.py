import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
num = list(map(int, input().split()))
num_lst = list(set(num))

num_lst.sort()

num_dict = dict()
for i in range(len(num_lst)):
    num_dict[num_lst[i]] = i

for i in num:
    print(num_dict[i], end=' ')