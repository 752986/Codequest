import sys

SEPARATOR = " "

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    line = sys.stdin.readline().rstrip()

	# replace this line as needed
    args = [val for val in line.split(SEPARATOR)]

    temp = float(args[0])
    if temp > 100:
        print("The planet is too hot.")
        continue
    elif temp < 0:
        print("The planet is too cold.")
        continue
    
    if args[1] != "true":
        print("The planet has no water.")
        continue

    if args[2] != "true":
        print("The planet has no magnetic field.")
        continue

    ecc = float(args[3])
    if ecc > 0.6:
        print("The planet's orbit is not ideal.")
        continue
    
    print("The planet is habitable.")