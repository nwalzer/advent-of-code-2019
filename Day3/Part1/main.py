import sys

f = open("input.txt", "r")
wire1 = f.readline().split(",")
wire2 = f.readline().split(",")
f.close()

wire1_path = {}
intersections = []
i = 0 #row
j = 0 #col
k = 0
for ele in wire1 :
    if ele[0] == 'R' :
        for col in range(int(ele[1:])):
            wire1_path[str(i) + ',' + str(j)] = 1
            k += 1
            j += 1
    elif ele[0] == 'L' :
        for col in range(int(ele[1:])):
            wire1_path[str(i) + ',' + str(j)] = 1
            k += 1
            j -= 1
    elif ele[0] == 'U' :
        for col in range(int(ele[1:])):
            wire1_path[str(i) + ',' + str(j)] = 1
            k += 1
            i += 1
    elif ele[0] == 'D' :
        for col in range(int(ele[1:])):
            wire1_path[str(i) + ',' + str(j)] = 1
            k += 1
            i -= 1

i = 0
j = 0
k = 0
for ele in wire2 :
    if ele[0] == 'R' :
        for col in range(int(ele[1:])):
            try:
                if wire1_path[str(i) + ',' + str(j)] == 1 :
                    intersections.append({'i': i, 'j': j})
            except:
                i = i
                #useless statement we don't care about
            k += 1
            j += 1
    elif ele[0] == 'L' :
        for col in range(int(ele[1:])):
            try:
                if wire1_path[str(i) + ',' + str(j)] == 1:
                    intersections.append({'i': i, 'j': j})
            except:
                i = i
                # useless statement we don't care about
            k += 1
            j -= 1
    elif ele[0] == 'U' :
        for col in range(int(ele[1:])):
            try:
                if wire1_path[str(i) + ',' + str(j)] == 1:
                    intersections.append({'i': i, 'j': j})
            except:
                i = i
                # useless statement we don't care about
            k += 1
            i += 1
    elif ele[0] == 'D' :
        for col in range(int(ele[1:])):
            try:
                if wire1_path[str(i) + ',' + str(j)] == 1:
                    intersections.append({'i': i, 'j': j})
            except:
                i = i
                # useless statement we don't care about
            k += 1
            i -= 1

minEle = {'i': sys.maxsize, 'j': sys.maxsize, 'manDist': sys.maxsize}
for ele in intersections :
    if ele['i'] == 0 and ele['j'] == 0:
        continue
    print(abs(ele['i']) + abs(ele['j']))
    if (abs(ele['i']) + abs(ele['j'])) < (abs(minEle['i']) + abs(minEle['j'])):
        minEle = {'i': ele['i'], 'j': ele['j'], 'manDist': abs(ele['i']) + abs(ele['j'])}

print("MINIMUM INTERSECTION IS: " + str(minEle))
