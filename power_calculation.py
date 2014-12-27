import math

N = input()
answers = []

for i in range(N):
    num = raw_input().split()
    k = int(num[0])
    n = int(num[1])

    sum = 0
    for i in range(1, k):
        sum += pow(i, n)
    
    digits = str(sum)[-2 : -1]
    if digits[0] == "":
        digits[0] == "0"
    if digits[1] == "":
        digits[1] == "0"
    print digits