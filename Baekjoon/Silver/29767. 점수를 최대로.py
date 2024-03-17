import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, K = map(int, input().split())

scores = list(map(int, input().split()))
scores_sum = 0
scores_sum_sort = []

for score in scores:
    scores_sum += score

    scores_sum_sort.append(scores_sum)

scores_sum_sort.sort(reverse=True)

answer = sum(scores_sum_sort[:K])

print(answer)