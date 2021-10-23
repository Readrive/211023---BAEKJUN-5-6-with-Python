N = int(input("수를 입력하세요"))

for i in range(N):
    arr=  input()
    score = 0
    sumScore = 0
    for j in arr:
        if j == 'O':
            score += 1
        else:
            score = 0
        sumScore += score
    print(sumScore)
