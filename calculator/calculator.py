import sys

SEPARATOR = " "

# python's built-in round function rounds to the nearest even number when the input is on a .5 boundary
# this function rounds always rounds up in that case, which is what codequest expects
def custom_round(number: float, ndigits: int = 0) -> float:
    number *= 10**ndigits
    result = int(number + (0.5 if number >= 0 else -0.5))
    return result / 10**ndigits

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    line = sys.stdin.readline().rstrip()

	# replace this line as needed
    args = [val for val in line.split(SEPARATOR)]

    n1 = float(args[0])
    n2 = float(args[2])

    if args[1] == "+":
        print(custom_round(n1 + n2, 1), custom_round(n2 + n1, 1))
    elif args[1] == "-":
        print(custom_round(n1 - n2, 1), custom_round(n2 - n1, 1))
    elif args[1] == "*":
        print(custom_round(n1 * n2, 1), custom_round(n2 * n1, 1))
    elif args[1] == "/":
        print(custom_round(n1 / n2, 1), custom_round(n2 / n1, 1))
    