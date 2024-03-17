'''
https://school.programmers.co.kr/learn/courses/30/lessons/120956

[문제]

머쓱이는 태어난 지 11개월 된 조카를 돌보고 있습니다.
조카는 아직 "aya", "ye", "woo", "ma" 네 가지 발음과 네 가지 발음을 조합해서 만들 수 있는 발음밖에 하지 못하고 연속해서 같은 발음을 하는 것을 어려워합니다.
문자열 배열 babbling이 매개변수로 주어질 때, 머쓱이의 조카가 발음할 수 있는 단어의 개수를 return하도록 solution 함수를 완성해주세요.


[제한사항]

- 1 ≤ babbling의 길이 ≤ 10
- 1 ≤ babbling[i]의 길이 ≤ 30
- 문자열은 알파벳 소문자로만 이루어져 있습니다.

'''

def solution(babbling):
    answer = 0
    for i in babbling:
        idx = 0
        result = 1
        flag = 0
        while idx < len(i):
            if i[idx] == 'a':
                if flag == 1:
                    result = 0
                    break
                if idx+3 <= len(i):
                    if i[idx:idx+3] == 'aya':
                        idx += 3
                        flag = 1
                    else:
                        result = 0
                        break
                else:
                    result = 0
                    break
            elif i[idx] == 'y':
                if flag == 2:
                    result = 0
                    break
                if idx+2 <= len(i):
                    if i[idx:idx+2] == 'ye':
                        idx += 2
                        flag = 2
                    else:
                        result = 0
                        break
                else:
                    result = 0
                    break
            elif i[idx] == 'w':
                if flag == 3:
                    result = 0
                    break
                if idx+3 <= len(i):
                    if i[idx:idx+3] == 'woo':
                        idx += 3
                        flag = 3
                    else:
                        result = 0
                        break
                else:
                    result = 0
                    break
            elif i[idx] == 'm':
                if flag == 4:
                    result = 0
                    break
                if idx+2 <= len(i):
                    if i[idx:idx+2] == 'ma':
                        idx += 2
                        flag = 4
                    else:
                        result = 0
                        break
                else:
                    result = 0
                    break
            else:
                result = 0
                break

        answer += result

    return answer