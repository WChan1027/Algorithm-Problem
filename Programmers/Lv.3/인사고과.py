def solution(scores):
    answer = 1
    scores_wanho = scores[0]
    scores.sort(reverse=True, key=lambda x: (x[0], x[1]))

    score1_max = 0
    score2_max = 0
    new_score2_max = 0
    for i in scores:
        if i[0] != score1_max:
            score1_max = i[0]
            score2_max = new_score2_max
        if i[1] >= score2_max:
            if i[1] > new_score2_max:
                new_score2_max = i[1]

            if sum(i) > sum(scores_wanho):
                answer += 1

        if i[0] > scores_wanho[0] and i[1] > scores_wanho[1]:
            return -1

    return answer