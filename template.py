import sys

SEPARATOR = " "

cases = int(sys.stdin.readline().rstrip())

for case_num in range(cases):
    line = sys.stdin.readline().rstrip()

	# replace this line as needed
    args = [val for val in line.split(SEPARATOR)]
    