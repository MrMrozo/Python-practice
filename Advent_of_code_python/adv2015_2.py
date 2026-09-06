input = open("advdata2015_2.txt", "r").read()

inputParts = input.splitlines()

def paperNeeded(inputParts):
    totalPaper = 0
    for line in inputParts:
        splitLine = line.split("x")
        l, w, h = map(int, splitLine)
        face1 = l * w
        face2 = w * h
        face3 = h * l
        totalPaper += 2 * face1 + 2 * face2 + 2 * face3 + min(face1, face2, face3)
    return totalPaper

print(paperNeeded(inputParts))


def ribbonNeeded(inputParts):
    totalRibbon = 0
    for line in inputParts:
        splitLine = line.split("x")
        l, w, h = map(int, splitLine)
        totalRibbon += 2 * (l + w + h - max(l, w, h)) + l * w * h
    return totalRibbon

print(ribbonNeeded(inputParts))