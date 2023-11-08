cases = int(input())

large_length = 5

for case_num in range(cases):
	line = input().rstrip()

	# replace this line as needed
	small, large, target = [int(val) for val in line.split(" ")]

	done = False

	total = 0
	while large > 0:
		potential = total + (large * large_length)
		if potential == target: # we can meet the length with only large bricks
			print("true")
			done = True
			break
		elif potential < target: # we can add another large brick
			total += large_length
			large -= 1
		else: # another large brick won't fit, check if small bricks can make up the distance 
			break
	# (this is outside of the loop so it doesn't run if we exited with large bricks only)
	if not done:
		remaining = target - total
		if small >= remaining: # we can fill the wall
			print("true")
		else: # the wall can't be filled
			print("false")