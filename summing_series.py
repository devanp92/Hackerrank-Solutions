N = input()
answers = []

for i in range(N):
    num = input()
    answer = num ** 2 % (10 ** 9 + 7)
    answers.append(answer)

for i in answers:
    print i