cases = int(input())

for case_num in range(cases):
    line = input().rstrip()

	# replace this line as needed
    turkeys, goats, horses = (int(val) for val in line.split(" "))
    
    print(2*turkeys + 4*goats + 4*horses)