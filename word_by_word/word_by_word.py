import math

cases = int(input())

for case_num in range(cases):
	# replace this line as needed
	n_lines = int(input())

	# input:
	text = ""
	for _ in range(n_lines):
		text += input().rstrip()

	# count words:
	lengths: list[int] = []
	word_len = 0
	for c in text:
		if c.isalpha():
			word_len += 1
		else:
			if word_len != 0:
				lengths.append(word_len)
			word_len = 0
	
	# average:
	avg_len = sum(lengths) / len(lengths)
	print(f"Average: {avg_len:.1f}")

	# median:
	med_len = (lengths[math.floor(len(lengths) / 2)] + lengths[math.ceil(len(lengths) / 2)]) / 2
	print(f"Median: {med_len:.1f}")

	# modes:
	# count each length
	counts: dict[int, int] = {}
	for length in lengths:
		if length in counts:
			counts[length] += 1
		else:
			counts[length] = 1
	# find modes
	max_count = 0
	modes: list[int] = []
	for length, count in counts.items():
		if count > max_count:
			# reset the list since those ones had a lower count
			max_count = count
			modes = [length]
		elif count == max_count:
			modes.append(length)
	modes.sort()
	# print
	print("Modes: ", end="")
	for i, length in enumerate(modes):
		print(length, end="")
		if i != len(modes) - 1:
			print(",", end="")
	print()

	# range:
	min_len = min(lengths)
	max_len = max(lengths)
	print(f"Range: {max_len - min_len}")

	# chart:
	for length in range(min_len, max_len + 1):
		print(f"{' ' if len(str(length)) == 1 else ''}{length}|", end="")
		if length in counts:
			print("x" * counts[length], end="")
		print()