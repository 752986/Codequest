import sys

SEPARATOR = " "

cases = int(sys.stdin.readline().rstrip())

for case_num in range(cases):
    n_bits = int(sys.stdin.readline().rstrip())

    for i in range(2**n_bits):
        result = bin(i).removeprefix("0b")
        print(("0" * (n_bits - len(result))) + result)