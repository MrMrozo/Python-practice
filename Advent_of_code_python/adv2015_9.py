from itertools import permutations

input = open("Advent_of_code_python/advdata2015_9.txt").read().strip().splitlines()

def routes(input):
    distances = {}
    locations = set()
    
    for line in input:
        parts = line.split(" = ")
        distance = int(parts[1])
        route = parts[0].split(" to ")
        loc1, loc2 = route[0], route[1]
        
        distances[(loc1, loc2)] = distance
        distances[(loc2, loc1)] = distance
        locations.add(loc1)
        locations.add(loc2)
    
    min_distance = float('inf')
    max_distance = float('-inf')
    
    for perm in permutations(locations):
        total_distance = 0
        for i in range(len(perm) - 1):
            total_distance += distances[(perm[i], perm[i + 1])]
        
        if total_distance < min_distance:
            min_distance = total_distance
        if total_distance > max_distance:
            max_distance = total_distance
    return min_distance, max_distance

print(routes(input))