cases = int(input())

for case_num in range(cases):
	line = input().rstrip()

	(call, response) = (val.lower() for val in line.split("|"))

	agent = True
	for char in response:
		if char.isalpha() and char.lower() not in call:
			agent = False
			break

	if agent:
		print("That's my secret contact!")
	else:
		print("You're not a secret agent!")
