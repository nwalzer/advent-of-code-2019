def build_path(start):
    path = {}
    path[start] = 1
    try:
        for ele in build_path(direct_orbs[start]):
            path[ele] = 1
        return path
    except Exception as e:
        return path


def recur_calc(key, stop):
    sum = 1  # include self
    if key == stop:
        return 0
    try:
        sum += recur_calc(direct_orbs[key], stop)
        return sum
    except Exception as e:
        return 0


if __name__ == "__main__":
    with open("input.txt") as f:
        orbs = f.readlines()

    direct_orbs = {}

    for orbit in orbs:
        parent = orbit.split(")")[0]
        orbiter = orbit.split(")")[1].rstrip('\n')
        direct_orbs[orbiter] = parent

    you_path = build_path('YOU')
    san_path = build_path('SAN')

    for key in san_path.keys():
        try:
            you_path[key]
            stopper = key
            break
        except Exception as e:
            continue
    print(recur_calc(direct_orbs['YOU'], stopper) + recur_calc(direct_orbs['SAN'], stopper))
