testCases = int(input())
answer = []
for test in range(testCases):
    numbers = input()
    bracketSize=int(numbers[0])
    finalString = '('*bracketSize + numbers[0]
    for i in range(len(numbers)-1):
        difference = int(numbers[i+1]) - int(numbers[i])
        if difference > 0:
            finalString = finalString + '('*(abs(difference)) + numbers[i+1]
            bracketSize = bracketSize + difference
        elif difference < 0:
            finalString = finalString + ')'*(abs(difference)) + numbers[i+1]
            bracketSize = bracketSize + difference
        else:
            finalString = finalString + numbers[i+1]
    finalString = finalString + ')'*bracketSize
    answer.append("Case #{}: {}".format(test+1,finalString))
for line in answer:
    print(line)