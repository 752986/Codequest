cases = int(input())

for case_num in range(cases):
	line = input().rstrip()

	# replace this line as needed
	axes = [float(val) for val in line.split(" ")]

	for i in range(3):
		new_num = axes[i] + 180
		if new_num < 0:
			new_num += 360
		elif new_num >= 360:
			new_num -= 360

		axes[i] = new_num

	x, y, z = (val for val in axes)

	# TODO: add leading zeroes
	print(f"{x:.2f} {y:.2f} {z:.2f}")