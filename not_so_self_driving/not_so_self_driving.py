cases = int(input())

for case_num in range(cases):
    line = input()

	# replace this line as needed
    (speed, distance) = (float(val) for val in line.split(":"))

    if speed == 0:
        print("SAFE")
    elif distance / speed <= 1:
        print("SWERVE")
    elif distance / speed <= 5:
        print("BRAKE")
    else:
        print("SAFE")
    
