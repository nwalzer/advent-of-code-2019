def recur_calc(key):
    sum = 1 #include self
    try:
        #print(key + " : " + str(direct_orbs[key]))
        #for ele in direct_orbs[key]:
        #    sum += 1
        #    sum += recur_calc(ele)
        sum += recur_calc(direct_orbs[key])
        #print("SUMMED " + key + ": " + str(sum))
        return sum
    except Exception as e:
        #print(e)
        #print("LEAF: [\'" + key + "\']")
        return 0

if __name__ == "__main__":
    with open("input.txt") as f:
        orbs = f.readlines()

    direct_orbs = {}

    for orbit in orbs:
        parent = orbit.split(")")[0]
        orbiter = orbit.split(")")[1].rstrip('\n')
        direct_orbs[orbiter] = parent
    sum = 0
    for key in direct_orbs.keys():
        #print(key)
        sum += recur_calc(key)

    print(sum)