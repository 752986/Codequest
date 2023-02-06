import sys

SEPARATOR = " "

cases = int(sys.stdin.readline().rstrip())


class RGB:
    COLORS = [
        "X", # 000
        "R", # 001
        "G", # 010
        "Y", # 011
        "B", # 100
        "M", # 101
        "C", # 110
        "W"  # 111
    ] #      ^ BGR

    def __init__(self, r: bool, g: bool, b: bool):
        # the RGB values are stored as the bits of an int
        # so combining two led values just means ORing them together
        # also, it makes it easy to look up the text format of the color

        num = 0
        num |= 0b001 if r else 0
        num |= 0b010 if g else 0
        num |= 0b100 if b else 0

        self.bits = num

    def update(self, other: "RGB"):
        self.bits |= other.bits

    def clear(self):
        self.bits = 0

    def __str__(self) -> str:
        return self.COLORS[self.bits]


class Led:
    def __init__(self, color: RGB, index: int, direction: int) -> None:
        self.color = color
        self.index = index
        self.direction = direction # left is -1, right is 1


for caseNum in range(cases):
    info = sys.stdin.readline().rstrip().split(SEPARATOR)
    n_lights = int(info[0])
    start_lit = int(info[1])
    runtime = int(info[2])

    leds: list[Led] = []

    for _ in range(start_lit):
        line = sys.stdin.readline().rstrip().split(SEPARATOR)

        color: RGB
        if line[0] == "R":
            color = RGB(True, False, False)
        elif line[0] == "G":
            color = RGB(False, True, False)
        else:
            color = RGB(False, False, True)

        index = int(line[1])

        direction = int(line[2])

        leds.append(Led(color, index, direction))

    for _ in range(runtime + 1):
        strip: list[RGB] = [RGB(False, False, False) for _ in range(n_lights)]

        for light in leds:
            strip[light.index].update(light.color)
        
        for color in strip:
            print(color, end="")
        print()

        if len(strip) > 1: # handle the 1-length strip edge case 
            for light in leds:
                if light.index + light.direction in [-1, len(strip)]:
                    light.direction *= -1
                light.index += light.direction
