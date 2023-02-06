import sys
import struct

SEPARATOR = " "


def get_bits(num: int, start: int, end: int) -> int:
    '''Get the specific bits of a number. `start` and `end` are offsets from the right.'''

    assert end > start

    length = end - start
    mask = ((1 << length) - 1)

    return (num >> start) & mask

def get_signed_bits(num: int, start: int, end: int) -> int:
    result = get_bits(num, start, end - 1)

    negative = (num >> (end - 1)) & 1
    sign_weight = 2**(end - start - 1)

    return result + (-sign_weight * negative)

def format_float(num: float) -> str:
    if num > 99999.99999 or num < 0.00001:
        result = f"{num:.5e}".split("+")
        if len(result[1]) < 3:
            result[1] = "+0" + result[1]
        return result[0] + result[1]
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

        if args[0] == "int":
            num = get_signed_bits(data, start, end)
            print(num)
        elif args[0] == "uint":
            num = get_bits(data, start, end)
            print(num)
        elif args[0] == "float":
            bits = get_bits(data, start, end)
            num = struct.unpack("f", struct.pack("I", bits))[0]
            print(format_float(num))
        elif args[0] == "double":
            bits = get_bits(data, start, end)
            num = struct.unpack("d", struct.pack("Q", bits))[0]
            print(format_float(num))
