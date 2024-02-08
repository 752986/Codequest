import math
import copy

def custom_round(number: float, ndigits: int = 0) -> float:
	'''Rounds how codequest expects you to (half away from zero). `number` is the input, and `ndigits` is the number of digits to round to.'''
	number *= 10**ndigits
	result = int(number + (0.5 if number >= 0 else -0.5))
	return result / 10**ndigits

class Point:
	x: float
	y: float

	def __init__(self, x: float, y: float):
		self.x = x
		self.y = y

	def printable(self) -> str:
		return f"{custom_round(self.x, 1):.1f} {custom_round(self.y, 1):.1f}"
	
	def distance(self, other: "Point"):
		dx = self.x - other.x
		dy = self.y - other.y
		return math.sqrt(dx*dx + dy*dy)
	
class Stop(Point):
	close_points: list[Point]

	def	__init__(self, x: float, y: float):
		super().__init__(x, y)
		self.close_points = []

	def update(self):
		if len(self.close_points) == 0:
			return
		
		total_x = 0
		total_y = 0

		for p in self.close_points:
			total_x += p.x
			total_y += p.y
		
		total_x /= len(self.close_points)
		total_y /= len(self.close_points)

		self.x = total_x
		self.y = total_y

		self.close_points = []


cases = int(input())

for case_num in range(cases):
	line = input().rstrip()

	# replace this line as needed
	n_landmarks, n_stops = (int(val) for val in line.split(" "))

	landmarks: list[Point] = []
	for _ in range(n_landmarks):
		x, y = (int(n) for n in input().split(" "))
		landmarks.append(Point(x, y))

	stops: list[Stop] = []
	for _ in range(n_stops):
		x, y = (int(n) for n in input().split(" "))
		stops.append(Stop(x, y))

	updated = True
	while updated:
		prev_stops = copy.deepcopy(stops)

		for l in landmarks:
			closest = min(stops, key=l.distance)
			closest.close_points.append(l)

		for s in stops:
			s.update()

		updated = False
		for i in range(len(stops)):
			if stops[i].printable() != prev_stops[i].printable():
				updated = True
				break

	for s in stops:
		print(s.printable())
