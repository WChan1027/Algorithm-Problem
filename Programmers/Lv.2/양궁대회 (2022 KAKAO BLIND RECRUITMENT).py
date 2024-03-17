def solution(n, info):
    answer = [-1]
    to_get_score = [i+1 for i in info if i <= n]
    max_score = 0

    # 점수 비교, 점수차 반환
    def check_score(apeach, lion):
        score_apeach, score_lion = 0, 0

        for i in range(10):
            if lion[i] > apeach[i]:
                score_lion += 10-i
            elif apeach[i]:
                score_apeach += 10-i

        result = score_lion - score_apeach
        return result

    # 완전탐색
    def lion_shots(start, lion):
        nonlocal n, max_score, info, answer
        new_lion = lion[:]
        new_lion[10] += n - sum(new_lion)
        result = check_score(info, new_lion)

        if max_score < result:
            max_score = result
            answer = new_lion
        elif max_score and max_score == result:
            for i in range(11):
                if new_lion[10-i] > answer[10-i]:
                    answer = new_lion
                    break
                elif new_lion[10-i] < answer[10-i]:
                    break

        # 재귀
        for i in range(start, 11):
            if sum(lion) + to_get_score[i] <= n:
                lion[i] = to_get_score[i]
                lion_shots(i+1, lion)
                lion[i] = 0

        return

    if sum(to_get_score) == 0:
        return answer
    lion_shots(0, [0] * 11)

    return answer

n = 9
info = [0, 0, 1, 2, 0, 1, 1, 1, 1, 1, 1]

print(solution(n, info))