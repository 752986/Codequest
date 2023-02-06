import sys

SEPARATOR = " "

cases = int(sys.stdin.readline().rstrip())

for case_num in range(cases):
    line = sys.stdin.readline().rstrip().split(SEPARATOR)

    hex_string = line[0]
    little_endian = line[1] == "LITTLE"

    bytes = [int("0x" + hex_string[i:i+2], base=0) for i in range(0, 8, 2)]

    if little_endian:
        bytes.reverse()

    result = 0
    for i, byte in enumerate(bytes):
        result |= byte << ((3 - i) * 8)
    
    print(result)
    