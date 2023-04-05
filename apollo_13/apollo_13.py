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

	strs: list[str] = []

	for num in axes:
		num_string = f"{num:.2f}"
		while len(num_string) < 6:
			num_string = "0" + num_string
		
		strs.append(num_string)

	x, y, z = (val for val in strs)

	# TODO: add leading zeroes
	print(f"{x} {y} {z}")