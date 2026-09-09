input = "cqjxjnds"

def nextPassword(input):
    if input[-1] == 'z':
        return nextPassword(input[:-1]) + 'a'
    return input[:-1] + chr(ord(input[-1]) + 1)


def newPassword(input):
    input = nextPassword(input)
    while True:
        for char in input:
            if char in ['i', 'o', 'l']:
                input = input.replace(char, chr(ord(char) + 1))
        doubles = 0
        for i in range(len(input) - 1):
            if input[i] == input[i + 1]:
                if doubles == 0:
                    first_double = input[i]
                    doubles += 1
                elif doubles == 1 and input[i] != first_double:
                    doubles += 1
            if doubles == 2:
                break
        if doubles < 2:
            input = nextPassword(input)
            continue
        for i in range(len(input) - 2):
            if ord(input[i]) + 1 == ord(input[i + 1]) and ord(input[i]) + 2 == ord(input[i + 2]):
                return input
        input = nextPassword(input)

print(newPassword(input))
print(newPassword(newPassword(input)))