for test_case in range(10):
    T = int(input())

    word = input()
    sentence = input()
    answer = 0

    for i in range(len(sentence) - len(word)+1):
        n = 0
        if sentence[i] == word[0]:
            for j in range(1, len(word)):
                if sentence[i+j] != word[j]:
                    n += 1
            if n == 0:
                answer += 1

    print(f'#{T} {answer}')