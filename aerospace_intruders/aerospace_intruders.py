from enum import Enum

cases = int(input())


class ShipClass(Enum):
	A = 0
	B = 1
	C = 2

	def get_speed(self) -> int:
		if self == ShipClass.A:
			return 10
		elif self == ShipClass.B:
			return 20
		elif self == ShipClass.C:
			return 30
		else:
			raise NotImplementedError("this should not ever happen")
		
def shipclass_from_string(string: str) -> ShipClass:
	if string == "A":
		return ShipClass.A
	elif string == "B":
		return ShipClass.B
	elif string == "C":
		return ShipClass.C
	else:
		raise ValueError
	

class Ship:
	def __init__(self, name: str, ship_class: ShipClass, coords: tuple[int, int]):
		self.name = name
		self.ship_class = ship_class
		self.x = coords[0]
		self.y = coords[1]

	def update(self):
		self.x -= self.ship_class.get_speed()
		

for case_num in range(cases):
	n_ships = int(input())

	ships: list[Ship] = []

	for ship_num in range(n_ships):
		line = input().rstrip()

		# replace this line as needed
		(left, right) = (val for val in line.split(":"))
		(name, ship_class) = (val for val in left.split("_"))
		coords: tuple[int, int] = tuple(int(val) for val in right.split(","))

		ships.append(Ship(name, shipclass_from_string(ship_class), coords))
	
	while len(ships) > 0:
		# sort by x descending, fallback sort by y ascending
		ships.sort(key=lambda s: s.y, reverse=True)
		ships.sort(key=lambda s: s.x)

		destroyed = ships[0]

		print(f"Destroyed Ship: {destroyed.name} xLoc: {destroyed.x}")

		ships.remove(destroyed)

		for ship in ships:
			ship.update()