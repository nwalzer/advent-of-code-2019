for i in range (100):
    for j in range (100):
        with open("input.txt") as f:
            to_process = f.read().split(",")
        to_process[1] = i
        to_process[2] = j
        to_process[3] = int(to_process[i]) + int(to_process[j])
        #print(to_process)
        for y in range(4, len(to_process), 4):
            x = int(to_process[y])
            if x == 1 :
                to_process[int(to_process[y+3])] = (int(to_process[int(to_process[y+1])]) + int(to_process[int(to_process[y+2])]))
            elif x == 2 :
                to_process[int(to_process[y+3])] = (int(to_process[int(to_process[y+1])]) * int(to_process[int(to_process[y+2])]))
            elif x == 99 :
                #print(to_process)
                if int(to_process[0]) == 19690720 :
                    print(to_process)
                    print("Found using: " + str(i) + " and " + str(j))
                    exit(0)
                break
            else :
                print("INVALID OPCODE: " + str(x))
                break

