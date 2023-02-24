class Post:
    def __init__(self, pos: tuple[float, float], number: int) -> None:
        self.pos = pos
        self.number = number

cases = int(input())
for case_num in range(cases):
	# replace this line as needed
    height, width, n_posts = (int(val) for val in input().split(" "))

    map: list[list[bool]] = [[False for _ in range(width)] for _  in range(height)] # a list of rows, indexed with map[y][x]
    posts: list[Post] = []

    # fill the map:
    for y in range(height): # y is 0 at the top and increases downwards
        line = input()
        for x in range(width): # x is 0 at the left and increases rightward 
            tile = line[x]
            if tile == "#":
                map[y][x] = True
            elif tile == " ":
                pass
            else:
                posts.append(Post((y, x), int(tile)))
