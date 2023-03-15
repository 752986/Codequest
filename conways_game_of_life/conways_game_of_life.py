import copy

def inbounds(coord: tuple[int, int]) -> bool:
	x, y = coord
	return (x >= 0 and y >= 0 and x < 10 and y < 10)

def print_map(map: list[list[bool]]):
	for row in map:
		for cell in row:
			print(1 if cell else 0, end="")
		print()

cases = int(input())

for case_num in range(cases):
	n_gens = int(input().rstrip())

	map = [[n == '1' for n in input().rstrip()] for _ in range(10)]

	for _ in range(n_gens):
		working = copy.deepcopy(map)

		for y, row in enumerate(map):
			for x in range(len(row)):
				total = 0
				for offset in [
					(-1, 1), 
					(0, 1),
					(1, 1),
					(-1, 0),
					(1, 0),
					(-1, -1),
					(0, -1),
					(1, -1)
				]:
					neighbor = (x + offset[0], y + offset[1])
					if inbounds(neighbor):
						total += 1 if map[neighbor[1]][neighbor[0]] else 0
				if total <= 1:
					working[y][x] = False # the cell is lonely
				elif total == 2:
					pass # the cell stays the same
				elif total == 3:
					working[y][x] = True # the cell becomes alive
				else:
					working[y][x] = False # the cell is overpopulated
		
		map = working

	print_map(map)
	# print()
