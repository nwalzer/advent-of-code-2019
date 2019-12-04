startIDX = 271973
endIDX = 785961
totalPasswords = 0
allIncrease = False
instances = []

for x in range(0, 10):
    instances.append(0)

for x in range(startIDX, endIDX):
    for i in range(0, 10):
        instances[i] = 0
    instances[int(str(x)[0])] += 1
    allIncrease = True
    for y in range(1, len(str(x))):
        instances[int(str(x)[y])] += 1
        if int(str(x)[y]) < int(str(x)[y-1]):
            allIncrease = False
            break

    if allIncrease == True:
        for ele in instances:
            if ele == 2:
                totalPasswords += 1
                break
print(totalPasswords)