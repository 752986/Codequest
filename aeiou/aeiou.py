cases = int(input())

for case_num in range(cases):
    line = input().rstrip()

    result = 0
    for char in line:
        if char in "aeiou":
            result += 1

    print(result)