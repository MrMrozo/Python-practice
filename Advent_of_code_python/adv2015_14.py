input1 = open("Advent_of_code_python/advdata2015_14.txt").read().strip().splitlines()
input2 = 2503

def reindeerRace(input1, input2):
    max_distance = 0
    for line in input1:
        parts = line.split()
        speed = int(parts[3])
        flying = int(parts[6])
        resting = int(parts[-2])
        distance = speed * flying * (input2 // (flying + resting)) + min(input2 % (flying + resting), flying) * speed
        if distance > max_distance:
            max_distance = distance
    return max_distance
print(reindeerRace(input1, input2))


def reindeerRace2(input1, input2):
    points = {}
    for line in input1:
        parts = line.split()
        points[(parts[0], int(parts[3]), int(parts[6]), int(parts[-2]))] = [0, 0]
    for i in range(input2):
        first = 0
        for key, value in points.items():
            if i % (key[2] + key[3]) < key[2]:
                value[0] += key[1]
            if value[0] > first:
                first = value[0]
        for _, value in points.items():
            if value[0] == first:
                value[1] += 1
    max_points = 0
    for value in points.values():
        if value[1] > max_points:
            max_points = value[1]
    return max_points

print(reindeerRace2(input1, input2))