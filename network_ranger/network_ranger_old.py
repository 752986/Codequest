import sys
import math

SEPARATOR = " "

cases = int(sys.stdin.readline().rstrip())


def ip_to_bin(ip: str) -> int:
    parts = [int(x) for x in ip.split(".")]

    result = 0
    for i, part in enumerate(parts):
        # put each byte into its place
        result |= part << (3 - i) * 8
    
    return result

def bin_to_ip(ip: int) -> str:
    # get the 4 bytes of the address
    parts = [(ip >> (8 * (3 - i))) & 0b11111111 for i in range(4)]

    result = ""
    for part in parts:
        result += str(part) + "."
    result = result.removesuffix(".")

    return result


for case_num in range(cases):
    n_addrs = int(sys.stdin.readline().rstrip())

    args = [sys.stdin.readline().rstrip() for _ in range(n_addrs)]

    addrs = [ip_to_bin(x) for x in args]

    xored = 0
    for addr in addrs:
        xored ^= addr

    # after xoring, all differing bits will be set to 1
    # log gets us the position (from the right) of the highest bit that is a 1 (zero-indexed)
    # we floor so that we have a clean int, and then subtract from 32 to get the length from the left side
    if xored == 0:
        matching_bits = 32
    else:
        matching_bits = 32 - math.floor(math.log(xored, 2)) - 1

    if xored == 0:
        low_addr = addrs[0]
    else:
        shift_amount = math.floor(math.log(xored, 2)) + 1
        # bitshift to zero out the differing bits
        low_addr = addrs[0] >> shift_amount << shift_amount
    
    # print(sorted(args, key=ip_to_bin)[0], end="")
    print(bin_to_ip(low_addr), end="")
    print("/", end="")
    print(matching_bits)
