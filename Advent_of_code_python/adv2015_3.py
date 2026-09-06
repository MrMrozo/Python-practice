input = open("Advent_of_code_python\\advdata2015_3.txt", "r").read().strip()

def houses(input):
    x, y = 0, 0
    visited = set()
    visited.add((x, y))
    for c in input:
        if c == '^':
            y += 1
        elif c == 'v':
            y -= 1
        elif c == '>':
            x += 1
        elif c == '<':
            x -= 1
        visited.add((x, y))
    return len(visited)

print(houses(input))

def houses2(input):
    x1, y1 = 0, 0
    x2, y2 = 0, 0
    visited = set()
    visited.add((x1, y1))
    for i, c in enumerate(input):
        if i % 2 == 0:
            if c == '^':
                y1 += 1
            elif c == 'v':
                y1 -= 1
            elif c == '>':
                x1 += 1
            elif c == '<':
                x1 -= 1
            visited.add((x1, y1))
        else:
            if c == '^':
                y2 += 1
            elif c == 'v':
                y2 -= 1
            elif c == '>':
                x2 += 1
            elif c == '<':
                x2 -= 1
            visited.add((x2, y2))
    return len(visited)

print(houses2(input))