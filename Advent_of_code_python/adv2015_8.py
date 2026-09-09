input = open("Advent_of_code_python/advdata2015_8.txt").read().strip().splitlines()

def instructions(input):
    total_code_chars = 0
    total_memory_chars = 0
    
    for line in input:
        total_code_chars += len(line)
        memory_string = eval(line)
        total_memory_chars += len(memory_string)
    
    return total_code_chars - total_memory_chars

print(instructions(input))


def encode_string(s):
    encoded = '"'
    for char in s:
        if char == '"':
            encoded += '\\"'
        elif char == '\\':
            encoded += '\\\\'
        else:
            encoded += char
    encoded += '"'
    return encoded

def instructions2(input):
    total_code_chars = 0
    total_encoded_chars = 0
    
    for line in input:
        total_code_chars += len(line)
        encoded_string = encode_string(line)
        total_encoded_chars += len(encoded_string)
    
    return total_encoded_chars - total_code_chars

print(instructions2(input))