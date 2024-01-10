cases = int(input())

for case_num in range(cases):
	cypher = input().rstrip()

	shifts = [int(val) for val in input().split()]#nested for loop but short, you can have an if statement withing the line of code
	directions = [int(val) for val in input().split()]

	result = ""
	this_shift = 0
	this_direction = 0

	for char in cypher:
		if not char.isalpha():
			# if the char is punctuation, don't process it
			result += char
			continue

		order = ord(char) - 65

		# print(shifts[this_shift] * (-1 if directions[this_direction] else 1), end=" ")
		decoded = (order + (shifts[this_shift] * (-1 if directions[this_direction] else 1))) % 26
		decodedfrfr = chr(decoded + 65)

		result += decodedfrfr

		this_shift = (this_shift + 1) % len(shifts)
		this_direction = (this_direction + 1) % len(directions)

	result = result.lower()

	print(result)
