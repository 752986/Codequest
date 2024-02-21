from copy import deepcopy

class Tile:
	zero: bool
	one: bool

	def __init__(self, zero: bool = True, one: bool = True):
		self.zero = zero
		self.one = one

	def is_decided(self) -> bool:
		return self.zero ^ self.one
	
	def is_valid(self) -> bool:
		return self.zero | self.one
	
	def opposite(self) -> "Tile":
		if not self.is_decided():
			raise ValueError("idiot")
		
		return Tile(True, False) if self.one else Tile(False, True)
	
	def __str__(self) -> str:
		return f"{"0" if self.zero else "-"}{"1" if self.one else "-"}"
	
	def __repr__(self) -> str:
		return str(self)
	
	def __eq__(self, other: object) -> bool:
		assert type(other) == Tile
		
		return self.zero == other.zero and self.one == other.one
		
class Board:
	class BoardIterator:
		board: "Board"
		i: int
		j: int

		def __init__(self, board: "Board"):
			self.board = board
			self.i = 0
			self.j = 0

		def __iter__(self) -> "Board.BoardIterator":
			return self

		def __next__(self) -> Tile:
			result = self.board[self.i, self.j]

			self.j = (self.j + 1) % self.board.size
			if self.j == 0:
				self.i = (self.i + 1) % self.board.size

				if self.i == 0:
					raise StopIteration
				
			return result

	data: list[list[Tile]]
	size: int

	def __init__(self, size: int):
		self.data = [[Tile() for _ in range(size)] for _ in range(size)]
		self.size = size

	def isValid(self) -> bool:
		pass #TODO!
	
	def __str__(self) -> str:
		result = ""
		for row in self.data:
			for tile in row:
				result += f"{tile} "
			result += "\n"
		
		return result[:-2]
	
	def __getitem__(self, key: tuple[int, int]) -> Tile:
		return self.data[key[0]][key[1]]
	
	def __setitem__(self, key: tuple[int, int], value: Tile):
		self.data[key[0]][key[1]] = value

	def __iter__(self) -> BoardIterator:
		return Board.BoardIterator(self)

	def __eq__(self, other: object) -> bool:
		assert type(other) == Board
		assert self.size == other.size

		for tile, otherTile in zip(self, other):
			if tile != otherTile:
				return False
		
		return True
		

cases = int(input())

for case_num in range(cases):
	size = int(input())

	board = Board(size)

	for i in range(size):
		line = input().rstrip()
		for j in range(size):
			if line[j] == "0":
				tile = Tile(True, False)
			elif line[j] == "1":
				tile = Tile(False, True)
			else:
				tile = Tile(True, True)

			board[i, j] = tile

	complex = False

	changed = True
	prev = deepcopy(board)
	while changed:
		# check and cap 2 in a row hoizontal
		for i in range(board.size):
			for j in range(board.size):
				if j > 0:
					if board[i, j].is_decided():
						if board[i, j] == board[i, j-1]:
							if j - 2 >= 0:
								board[i, j-2] = board[i, j].opposite()
							if j + 1 < board.size:
								board[i, j+1] = board[i, j].opposite()

		# check and cap 2 in a row vertical
		for i in range(board.size):
			for j in range(board.size):
				if i > 0:
					if board[i, j].is_decided():
						if board[i, j] == board[i-1, j]:
							if i - 2 >= 0:
								board[i-2, j] = board[i, j].opposite()
							if i + 1 < board.size:
								board[i+1, j] = board[i, j].opposite()

		#TODO: check if board is in an invalid state

		if board == prev:
			changed = False
		prev = deepcopy(board)

	print(board)
	print()
