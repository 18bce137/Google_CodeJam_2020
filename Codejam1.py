testCases = int(input().strip())
answer = []
for test in range(testCases):
    repeatedRow = 0
    repeatedCol = 0
    N = int(input().strip())
    matrix = []
    for elements in range(N):
        matrix.append([int(x) for x in input().strip().split(" ")])
    trace = 0
    for elements in range(N):
        trace = trace + matrix[elements][elements]
    for row in matrix:
        seen = set(row)
        if len(seen)<len(row):
            repeatedRow = repeatedRow + 1
    for index in range(N):
        col=[]
        for row in matrix:
            col.append(row[index])
        seen = set(col)
        if len(seen)<len(col):
            repeatedCol = repeatedCol + 1
    answer.append("Case #{}: {} {} {}".format(test+1,trace,repeatedRow,repeatedCol))
for line in answer:
    print(line)