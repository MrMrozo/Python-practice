input = "3113322113"

def lookAndSay(input, times):
    for _ in range(times):
        result = ""
        index = 1
        for i in range(len(input)):
            if i != 0 and input[i] == input[i - 1]:
                continue
            char = input[i]
            count = 1
            while index < len(input) and char == input[index]:
                count += 1
                index += 1
            result += str(count) + char
            index += 1
        input = result
    return result

print(len(lookAndSay(input, 50)))