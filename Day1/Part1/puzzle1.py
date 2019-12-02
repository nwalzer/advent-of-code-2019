import math

sum = 0
f = open("puzzle1.txt", "r")

for line in f:
    x = int(line)
    x = math.floor(x / 3)
    print(str(int(line)) + " : " + str(int(line) / 3) + " : " + str(x))
    x -= 2
    sum += x

print(sum)