import sys

SEPARATOR = " "

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    line = sys.stdin.readline().rstrip()

	# replace this line as needed
    args = [val for val in line.split(SEPARATOR)]

    try:
        num = float(args[0])
    except ValueError:
        print("Invalid Dividend")
        continue

    try:
        den = float(args[1])
    except ValueError:
        print("Invalid Divisor")
        continue

    try:
        print(round(num / den, 1))
    except ZeroDivisionError:
        print("Divide By Zero")

    