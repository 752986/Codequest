# WARNING: some aspect of the type hints in this file makes codequest not like it, so remove them before you submit this

cases = int(input())

def num_from_at_bat(at_bat: str) -> int | None:
	'''Returns the weighted score for the given symbol. If the symbol has no weight, returns `None`. `at_bat` must be one of: \"BB\", \"K\", \"1B\", \"2B\", \"3B\", \"HR\", otherwise it raises an exception'''
	at_bat = at_bat.lower().strip()
	if at_bat == "bb":
		return None
	elif at_bat == "k":
		return 0
	elif at_bat == "1b":
		return 1
	elif at_bat == "2b":
		return 2
	elif at_bat == "3b":
		return 3
	elif at_bat == "hr":
		return 4
	else:
		raise ValueError("`at_bat` must be one of: \"BB\", \"K\", \"1B\", \"2B\", \"3B\", \"HR\"")

for case_num in range(cases):
	line = input().rstrip()

	player, hits = line.split(":")

	hit_nums = [num_from_at_bat(at_bat) for at_bat in hits.split(",")] # SAFE: guaranteed correct values by problem statement

	# filtered_hits: list[int] = list(filter(lambda val: val != None, hit_nums)) # unused because type checker doesn't like this way

	filtered_hits: list[int] = []
	for val in hit_nums:
		if val != None:
			filtered_hits.append(val)

	if len(filtered_hits) == 0:
		avg = 0
	else:
		avg = sum(filtered_hits) / len(filtered_hits) # SAFE: can't divide by zero since we check for that

	print(f"{player}={avg:.3f}")
