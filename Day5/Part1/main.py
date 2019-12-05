with open("input.txt") as f:
    to_process = f.read().split(",")

y = 0
while int(to_process[y]) != 99:
    parameter_types = ['0', '0']
    if len(str(to_process[y])) == 3:
        parameter_types[0] = str(to_process[y])[0]
    elif len(str(to_process[y])) == 4:
        parameter_types[0] = str(to_process[y])[1]
        parameter_types[1] = str(to_process[y])[0]
    #print(str(to_process[y]) + " --- " + str(parameter_types))

    x = int(to_process[y])%100
    if x == 1 :
        param1 = 0
        if parameter_types[0] == '0':
            param1 = int(to_process[int(to_process[y + 1])])
        else :
            param1 = int(to_process[y + 1])

        param2 = 0
        if parameter_types[1] == '0':
            param2 = int(to_process[int(to_process[y + 2])])
        else :
            param2 = int(to_process[y + 2])

        to_process[int(to_process[y+3])] = param1 + param2
        #print("STORED " + str(param1) + " " + str(param2) + " AT " +  str(to_process[y+3]))
        y += 4
    elif x == 2 :
        param1 = 0
        if parameter_types[0] == '0':
            param1 = int(to_process[int(to_process[y + 1])])
        else:
            param1 = int(to_process[y + 1])

        param2 = 0
        if parameter_types[1] == '0':
            param2 = int(to_process[int(to_process[y + 2])])
        else:
            param2 = int(to_process[y + 2])

        to_process[int(to_process[y + 3])] = param1 * param2
        y += 4
    elif x == 3 :
        to_process[int(to_process[y + 1])] = int(input("Enter value: "))
        #print("STORED AT " + str(to_process[y + 1]))
        y += 2
    elif x == 4 :
        if parameter_types[0] == '0':
            print("POS " + str(int(to_process[y + 1])) + " : " + str(to_process[int(to_process[y + 1])]))
        else :
            print("POS " + str(int(to_process[y + 1])) + " : " + str(to_process[y + 1]))
        y += 2
    elif x == 99 :
        print(to_process)
        exit(0)
        break
    else :
        print("INVALID OPCODE: " + str(x))
        exit(1)
        break

print("FINISHED")