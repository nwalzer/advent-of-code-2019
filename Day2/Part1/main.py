with open("input.txt") as f:
    to_process = f.read().split(",")
for y in range(4, len(to_process), 4):
    x = int(to_process[y])
    if x == 1 :
        to_process[int(to_process[y+3])] = (int(to_process[int(to_process[y+1])]) + int(to_process[int(to_process[y+2])]))
    elif x == 2 :
        to_process[int(to_process[y+3])] = (int(to_process[int(to_process[y+1])]) * int(to_process[int(to_process[y+2])]))
    elif x == 99 :
        print(to_process)
        exit(0)
        break
    else :
        print("INVALID OPCODE: " + str(x))
        exit(1)
        break

