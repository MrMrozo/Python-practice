input = open("Advent_of_code_python/advdata2015_5.txt").read().strip().splitlines()

def isNice(string):
    vowels = "aeiou"
    vowelCount = sum(1 for char in string if char in vowels)
    hasDoubleLetter = any(string[i] == string[i + 1] for i in range(len(string) - 1))
    hasForbiddenSubstrings = any(substring in string for substring in ["ab", "cd", "pq", "xy"])
    
    return vowelCount >= 3 and hasDoubleLetter and not hasForbiddenSubstrings

niceCount = sum(1 for line in input if isNice(line))
print(niceCount)

def isNice2(string):
    hasPair = any(string[i:i + 2] in string[i + 2:] for i in range(len(string) - 1))
    hasRepeatWithOneBetween = any(string[i] == string[i + 2] for i in range(len(string) - 2))
    
    return hasPair and hasRepeatWithOneBetween

print(sum(1 for line in input if isNice2(line)))