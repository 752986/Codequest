cases = int(input())

for case_num in range(cases):
    line = input().rstrip()

	# replace this line as needed
    (a, b) = (list(val) for val in line.split("|"))
    
    anagram = True

    if a == b:
        anagram = False
    else:
        for char in a:
            if char in b:
                a.remove(char)
                b.remove(char)
            else:
                anagram = False
                break
    
    if anagram:
        print(line + " = ANAGRAM")
    else:
        print(line + " = NOT AN ANAGRAM")