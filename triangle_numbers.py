N = input()

answers = []
for i in range(N):
    num_row = input()

    if num_row % 2 == 1:
        answers.append(2)
    elif num_row % 4 == 0:
        answers.append(3)
    elif num_row % 4 == 2:
        answers.append(4)
    else:
        answers.append(-1)

for i in answers:
    print i

