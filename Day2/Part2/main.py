
f = open("input.txt", "r")

to_process = f.read().split(",")
for y in range(0, len(to_process), 4):
    x = int(to_process[y])
    if x == 1 :
        #print(to_process[int(to_process[y + 1])] + to_process[int(to_process[y + 2])])
        to_process[int(to_process[y+3])] = (int(to_process[int(to_process[y+1])]) + int(to_process[int(to_process[y+2])]))
        #print(to_process[to_process[y+3]])
    elif x == 2 :
        to_process[int(to_process[y+3])] = (int(to_process[int(to_process[y+1])]) * int(to_process[int(to_process[y+2])]))
    elif x == 99 :
        print("FINISHED")
        print(to_process)
        exit(0)
    else :
        print("INVALID OPCODE: " + str(x))
        exit(1)

