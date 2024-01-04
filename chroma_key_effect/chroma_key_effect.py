import math

cases = int(input())

def colorAbs(r: int, g: int, b: int) -> float:
	return math.sqrt(r*r + g*g + b*b)

for case_num in range(cases):
	line = input().rstrip()

	# replace this line as needed
	keyR, keyG, keyB, tolerance, fgR, fgG, fgB, bgR, bgG, bgB = (int(val) for val in line.split(" "))

	if colorAbs(fgR - keyR, fgG - keyG, fgB - keyB) <= tolerance:
		print(f"{bgR} {bgG} {bgB}")
	else:
		print(f"{fgR} {fgG} {fgB}")