def Sort(sub_li):
    l = len(sub_li)
    for i in range(0, l):
        for j in range(0, l-i-1):
            if (sub_li[j][0] > sub_li[j + 1][0]):
                tempo = sub_li[j]
                sub_li[j]= sub_li[j + 1]
                sub_li[j + 1]= tempo
    return sub_li
testCases = int(input())
answer = []
for test in range(testCases):
    tasks = int(input())
    finalString = ""
    tasklist = []
    for elements in range(tasks):
        tasklist.append([int(x) for x in input().strip().split(" ")])
    i=0
    for elements in tasklist:
        elements.append(i)
        i+=1
    SortedTasklist = Sort(tasklist)
    Cameron = []
    CameronEndTime = 0
    Jamie = []
    JamieEndTime = 0
    response = dict()
    for task in SortedTasklist:
        if task[0] >= CameronEndTime:
            CameronEndTime = task[1]
            response[task[2]] = 'C'
        elif task[0] >= JamieEndTime:
            JamieEndTime = task[1]
            response[task[2]] = 'J'
        else:
            response[task[2]] = 'F'
    for task in range(tasks):
        if response[task] == 'C':
            finalString = finalString + 'C'
        elif response[task] == 'J':
            finalString = finalString + 'J'
        else:
            finalString = 'IMPOSSIBLE'
            break
    answer.append("Case #{}: {}".format(test+1,finalString))
for line in answer:
    print(line)
