cases = int(input())

for case_num in range(cases):
	line = input().rstrip()

	hours = "00"
	minutes = "00"
	seconds = "00"

	current_char = 0
	while current_char < len(line):
		char = line[current_char]
		if char.isdigit():
			number = ""
			while char.isdigit():
				number += char
				current_char += 1
				char = line[current_char]

			if char == "h":
				hours = number.zfill(2)
			elif char == "m":
				minutes = number.zfill(2)
			elif char == "s":
				seconds = number.zfill(2)

		current_char += 1


	print(f"{hours:}:{minutes:}:{seconds:}")