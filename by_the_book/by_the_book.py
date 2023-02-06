import sys

SEPARATOR = " "

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    line = sys.stdin.readline().rstrip()

    checksum = 0
    for i in range(9):
        checksum += int(line[i]) * (10 - i)
    
    check_digit = 10 if line[9] == "X" else int(line[9])

    result = (checksum + check_digit) % 11 == 0
    
    print("VALID" if result else "INVALID")