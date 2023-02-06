import sys

SEPARATOR = " "

MULTIPLIERS = [
    8,
    4,
    2,
    1
]

VALUES = [
    "off",
    "red",
    "green",
    "blue"
]

cases = int(sys.stdin.readline().rstrip())
for caseNum in range(cases):
    line = sys.stdin.readline().rstrip()

	# replace this line as needed
    args = [val == "WORKING" for val in line.split(SEPARATOR)]
    assert len(args) == 4
    
    total = 0
    for i, working in enumerate(args):
        total += MULTIPLIERS[i] if not working else 0
    
    print(VALUES[total // 4], VALUES[total % 4])