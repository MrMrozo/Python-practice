input = "ckczppom"

import hashlib

def md5_number(input):
    number = 0
    while True:
        test_string = input + str(number)
        md5_hash = hashlib.md5(test_string.encode()).hexdigest()
        if md5_hash.startswith("00000"):
            return number
        number += 1

print(md5_number(input))

def md5_number2(input):
    number = 0
    while True:
        test_string = input + str(number)
        md5_hash = hashlib.md5(test_string.encode()).hexdigest()
        if md5_hash.startswith("000000"):
            return number
        number += 1

print(md5_number2(input))