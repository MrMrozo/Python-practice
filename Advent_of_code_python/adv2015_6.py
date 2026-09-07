input = open("Advent_of_code_python/advdata2015_6.txt").read().strip().splitlines()

def instructions(input):
    grid = [[0] * 1000 for _ in range(1000)]
    
    for line in input:
        parts = line.split()
        if parts[0] == "turn":
            action = parts[1]
            start = tuple(map(int, parts[2].split(',')))
            end = tuple(map(int, parts[4].split(',')))
        elif parts[0] == "toggle":
            action = "toggle"
            start = tuple(map(int, parts[1].split(',')))
            end = tuple(map(int, parts[3].split(',')))
        
        for i in range(start[0], end[0] + 1):
            for j in range(start[1], end[1] + 1):
                if action == "on":
                    grid[i][j] = min(1, grid[i][j] + 1)
                elif action == "off":
                    grid[i][j] = max(0, grid[i][j] - 1)
                elif action == "toggle":
                    grid[i][j] = 1 - grid[i][j]

    return sum(sum(row) for row in grid)

print(instructions(input))

def instructions2(input):
    grid = [[0] * 1000 for _ in range(1000)]
    
    for line in input:
        parts = line.split()
        if parts[0] == "turn":
            action = parts[1]
            start = tuple(map(int, parts[2].split(',')))
            end = tuple(map(int, parts[4].split(',')))
        elif parts[0] == "toggle":
            action = "toggle"
            start = tuple(map(int, parts[1].split(',')))
            end = tuple(map(int, parts[3].split(',')))
        
        for i in range(start[0], end[0] + 1):
            for j in range(start[1], end[1] + 1):
                if action == "on":
                    grid[i][j] += 1
                elif action == "off":
                    grid[i][j] = max(0, grid[i][j] - 1)
                elif action == "toggle":
                    grid[i][j] += 2

    return sum(sum(row) for row in grid)

print(instructions2(input))