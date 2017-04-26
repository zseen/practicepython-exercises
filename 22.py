counterDict = {}
with open('nameslist.txt') as f:
    line = f.readline()
    while line:
        line = line.strip()
        if line in counterDict:
            counterDict[line] += 1
        else:
            counterDict[line] = 1
        line = f.readline()

print(counterDict)
