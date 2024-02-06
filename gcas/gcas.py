#TODO: this problem might want you to extrapolate the velocities over time

ALT = 0
GND = 1

cases = int(input())

for case_num in range(cases):
	flight_time = int(input())

	# collect data:
	data: list[tuple[int, int]] = [(0, 0)]

	gnd = 0
	for _ in range(flight_time):
		alt, new_gnd = map(int, input().split(","))

		data.append((alt, gnd))

		gnd = new_gnd
	data.append((0, gnd))

	# analysis:
	for i in range(1, len(data) - 1):
		slope = data[i][ALT] - data[i - 1][ALT]
		predicted = data[i][ALT] + slope # predicted altitude next time unit
		if predicted < data[i + 1][GND]:
			print("PULL UP!")
		elif data[i][ALT] - 500 <= data[i][GND]:
			print("Low Altitude!")
		else:
			print("ok")
