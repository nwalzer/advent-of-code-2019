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
            wire1_path[str(i) + ',' + str(j)] = k
            k += 1
            j += 1
    elif ele[0] == 'L' :
        for col in range(int(ele[1:])):
            wire1_path[str(i) + ',' + str(j)] = k
            k += 1
            j -= 1
    elif ele[0] == 'U' :
        for col in range(int(ele[1:])):
            wire1_path[str(i) + ',' + str(j)] = k
            k += 1
            i += 1
    elif ele[0] == 'D' :
        for col in range(int(ele[1:])):
            wire1_path[str(i) + ',' + str(j)] = k
            k += 1
            i -= 1

i = 0
j = 0
k = 0
for ele in wire2 :
    if ele[0] == 'R' :
        for col in range(int(ele[1:])):
            try:
                length = wire1_path[str(i) + ',' + str(j)]
                intersections.append({'i': i, 'j': j, 'totalLen': k + length})
            except:
                i = i
                #useless statement we don't care about
            k += 1
            j += 1
    elif ele[0] == 'L' :
        for col in range(int(ele[1:])):
            try:
                length = wire1_path[str(i) + ',' + str(j)]
                intersections.append({'i': i, 'j': j, 'totalLen': k + length})
            except:
                i = i
                # useless statement we don't care about
            k += 1
            j -= 1
    elif ele[0] == 'U' :
        for col in range(int(ele[1:])):
            try:
                length = wire1_path[str(i) + ',' + str(j)]
                intersections.append({'i': i, 'j': j, 'totalLen': k + length})
            except:
                i = i
                # useless statement we don't care about
            k += 1
            i += 1
    elif ele[0] == 'D' :
        for col in range(int(ele[1:])):
            try:
                length = wire1_path[str(i) + ',' + str(j)]
                intersections.append({'i': i, 'j': j, 'totalLen': k + length})
            except:
                i = i
                # useless statement we don't care about
            k += 1
            i -= 1

minEle = {'i': 0, 'j': 0, 'totalLen': sys.maxsize}
for ele in intersections :
    if ele['i'] == 0 and ele['j'] == 0:
        continue
    print(str(abs(ele['i']) + abs(ele['j'])) + ': ' + str(ele['totalLen']))
    if ele['totalLen'] < minEle['totalLen']:
        minEle = ele

print("THE MINIMUM PATH LENGTH IS: " + str(minEle))
