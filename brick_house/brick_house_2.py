cases = int(input())

large_length = 5

for case_num in range(cases):
	line = input().rstrip()

	# replace this line as needed
	small, large, target = [int(val) for val in line.split(" ")]

	