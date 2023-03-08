cases = int(input())

for case_num in range(cases):
    line = input().rstrip()

	# replace this line as needed
    (a, b) = (int(val) for val in line.split(" "))

    print(a + b, a * b)
    