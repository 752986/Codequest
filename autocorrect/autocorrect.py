cases = int(input())

def hamming_dist(s1: str, s2: str) -> int:
	assert len(s1) == len(s2)

	dist = 0
	for i in range(len(s1)):
		if s1[i] != s2[i]:
			dist += 1

	return dist

for case_num in range(cases):
	line = input().rstrip()
	(n_words, n_test) = (int(val) for val in line.split(" "))

	words: list[str] = []

	for _ in range(n_words):
		words.append(input().rstrip())
	
	for _ in range(n_test):
		test = input().rstrip()

		dists: list[tuple[str, int]] = []

		for word in words:
			if len(test) == len(word):
				dists.append((word, hamming_dist(test, word)))

		dists.sort(key=lambda t: t[1])
		
		print(dists[0][0])