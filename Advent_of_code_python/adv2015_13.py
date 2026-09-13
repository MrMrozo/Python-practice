from itertools import permutations

input = open("Advent_of_code_python/advdata2015_13.txt").read().strip().splitlines()

def sitting(input):
    happiness = {}
    guests = set()
    
    for line in input:
        parts = line.split()
        happyNet = int(parts[3])
        if parts[2] == "lose":
            happyNet *= -1
        guest1, guest2 = parts[0], parts[-1][:-1]
        guests.add(guest1)
        guests.add(guest2)

        if (guest2, guest1) in happiness:
            happiness[(guest2, guest1)] += happyNet
        else:
            happiness[(guest1, guest2)] = happyNet

    max_happy = float("-inf")

    for perm in permutations(guests):
        perm = perm + perm[0:1]
        total_happiness = 0
        for i in range(len(perm) - 1):
            if (perm[i], perm[i + 1]) in happiness:
                total_happiness += happiness[(perm[i], perm[i + 1])]
            else:
                total_happiness += happiness[(perm[i + 1], perm[i])]
        if total_happiness > max_happy:
            max_happy = total_happiness
    return max_happy

print(sitting(input))


def sitting2(input):
    happiness = {}
    guests = set()
    
    for line in input:
        parts = line.split()
        happyNet = int(parts[3])
        if parts[2] == "lose":
            happyNet *= -1
        guest1, guest2 = parts[0], parts[-1][:-1]
        guests.add(guest1)
        guests.add(guest2)

        if (guest2, guest1) in happiness:
            happiness[(guest2, guest1)] += happyNet
        else:
            happiness[(guest1, guest2)] = happyNet

    max_happy = float("-inf")

    for perm in permutations(guests):
        perm = perm + perm[0:1]
        total_happiness = 0
        for i in range(len(perm) - 1):
            yourSeat = float("inf")
            if (perm[i], perm[i + 1]) in happiness:
                key = (perm[i], perm[i + 1])
            else:
                key = (perm[i + 1], perm[i])
            total_happiness += happiness[key]
            if happiness[key] < yourSeat:
                yourSeat = happiness[key]

        total_happiness -= yourSeat
        if total_happiness > max_happy:
            max_happy = total_happiness
    return max_happy

print(sitting2(input))