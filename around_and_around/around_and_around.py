import math

def custom_round(number: float, ndigits: int = 0) -> float:
	'''Rounds how codequest expects you to (half away from zero). `number` is the input, and `ndigits` is the number of digits to round to.'''
	number *= 10**ndigits
	result = int(number + (0.5 if number >= 0 else -0.5))
	return result / 10**ndigits

cases = int(input())

for case_num in range(cases):
	altitude = int(input())

	distance = altitude * 2 * math.pi + 40075

	print(custom_round(distance, 1))