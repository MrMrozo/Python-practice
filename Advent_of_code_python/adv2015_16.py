import string

input1 = open("Advent_of_code_python/advdata2015_16.txt").read().strip().splitlines()
input2 = open("Advent_of_code_python/advdata2015_16_2.txt").read().strip().splitlines()


def sue(input1, input2):
    realSue = {}
    for line in input2:
        words = line.split()
        realSue[words[0]] = words[1]
    for line in input1:
        words = line.split()
        if realSue[words[2]] == words[3][:-1] and realSue[words[4]] == words[5][:-1] and realSue[words[6]] == words[7]:
            return int(words[1][:-1])

print(sue(input1, input2))



def sue2(input1, input2):
    realSue = {}
    for line in input2:
        words = line.split()
        realSue[words[0][:-1]] = int(words[1])
    for line in input1:
        line = line.translate(str.maketrans('', '', string.punctuation))
        words = line.split()
        flags = 0
        for i in [2,4,6]:
            match words[i]:
                case "cats" | "trees":
                    if realSue[words[i]] < int(words[i + 1]):
                        flags += 1
                case "pomeranians" | "goldfish":
                    if realSue[words[i]] > int(words[i + 1]):
                        flags += 1
                case _:
                    if realSue[words[i]] == int(words[i + 1]):
                        flags += 1
        if flags == 3:
            return int(words[1])
        
print(sue2(input1, input2))