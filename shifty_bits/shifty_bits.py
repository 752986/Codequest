import sys
import struct

SEPARATOR = " "


def get_bits(num: int, start: int, end: int) -> int:
    '''Get the specific bits of a number. `start` and `end` are offsets from the right.'''

    assert end >= start # POTENTIAL ERROR: if this is false, then something has gone wrong

    length = end - start
    mask = ((1 << length) - 1)

    return (num >> start) & mask # bitshift to get rid of right bits, then mask to get rid of left bits


def get_signed_bits(num: int, start: int, end: int) -> int:
    '''Get the specific bits of a number, and treat it as a two's compliment signed int. `start` and `end` are offsets from the right.'''

    assert end > start # >= might work here, but I'm not sure # POTENTIAL ERROR: if this is false, then something has gone wrong

    result = get_bits(num, start, end - 1)

    negative = (num >> (end - 1)) & 1
    sign_weight = 2**(end - start - 1)

    return result + (-sign_weight * negative)


def format_float(num: float) -> str:
    if abs(num) > 99999.99999 or abs(num) < 0.00001:
        result = f"{num:.5e}".split("e")

        if len(result[1]) == 3:
            result[1] = result[1][0] + "0" + result[1][1:]

        return result[0] + "e" + result[1]
    else:
        return f"{num:.5f}"


cases = int(sys.stdin.readline().rstrip())

for case_num in range(cases):
    data = sys.stdin.readline().rstrip().removeprefix("0x")
    data = int(data, 16)
    n_data = int(sys.stdin.readline().rstrip())

    for i in range(n_data):
        line = sys.stdin.readline().rstrip()
        args = [val for val in line.split(SEPARATOR)]

        data_type = args[0]

        start = int(args[1])
        end = start + int(args[2])

        if data_type == "int":
            num = get_signed_bits(data, start, end)
            print(num)
        elif data_type == "uint":
            num = get_bits(data, start, end)
            print(num)
        elif data_type == "float":
            bits = get_bits(data, start, end)
            num = struct.unpack("f", struct.pack("I", bits))[0] # POTENTIAL ERROR: if the wrong number of bits is given, but that shouldn't happen
            print(format_float(num))
        elif data_type == "double":
            bits = get_bits(data, start, end)
            num = struct.unpack("d", struct.pack("Q", bits))[0] # POTENTIAL ERROR: if the wrong number of bits is given, but that shouldn't happen
            print(format_float(num))
