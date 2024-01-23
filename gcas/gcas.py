#TODO: this problem might want you to extrapolate the velocities over time

cases = int(input())

for case_num in range(cases):
	flight_time = int(input())

	gnd = 0
	for _ in range(flight_time):
		alt, new_gnd = map(int, input().split(","))

		if alt < new_gnd:
			print("PULL UP!")
		elif alt - 500 <= gnd:
			print("Low Altitude!")
		else:
			print("ok")

		gnd = new_gnd
