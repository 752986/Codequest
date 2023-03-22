import math

cases = int(input())

for case_num in range(cases):
	n_rocks = int(input())

	rocks: list[tuple[int, int]] = []

	for _ in range(n_rocks):
		rock = tuple(int(val) for val in input().rstrip().split(" "))
		assert len(rock) == 2

		rocks.append(rock)

	rocks.sort(key = lambda pos: math.sqrt(pos[0]**2 + pos[1]**2))

	for result in rocks:	
		print(result[0], result[1])