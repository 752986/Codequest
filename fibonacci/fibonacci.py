# this function uses memoization to speed it up by a *lot*
fib_results: dict[int, int] = {0: 0, 1: 1}
def fib(n: int) -> int:
	global fib_results
	if n in fib_results:
		return fib_results[n]
	else:
		result = fib(n - 1) + fib(n - 2)
		fib_results[n] = result
		return result

def fib2(n: int) -> int:
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fib2(n - 1) + fib2(n - 2)


cases = int(input())

for case_num in range(cases):
	num = int(input())
	# for comparison, try using `fib2` instead of `fib` here
	print(f"{num} = {fib2(num - 1)}")

