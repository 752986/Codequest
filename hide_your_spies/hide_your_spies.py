import sys

SEPARATOR = " "


class Line:
    def __init__(self, p1: tuple[float, float], p2: tuple[float, float]):
        if p1[0] != p2[0]:
            self.slope = (p2[1] - p1[1]) / (p2[0] - p1[0])
            self.vertical = False
            self.intercept = self.slope * -p1[0] + p1[1]
        else: 
            # if the line is vertical, then slope is zero and intercept stores the x coordinate
            self.slope = 0
            self.vertical = True
            self.intercept = p1[0]

        self.bounds = (p1, (p2[0] - p1[0], p2[1] - p1[1]))

    def intersection(self, other: "Line") -> tuple[float, float] | None:
        if self.slope == other.slope:
            return None

        if self.vertical:
            x = self.intercept
            y = (other.slope * x) + other.intercept
        elif other.vertical:
            x = other.intercept
            y = (self.slope * x) + self.intercept
        else:
            x = (other.intercept - self.intercept) / (self.slope - other.slope)
            y = (self.slope * x) + self.intercept

        return (x, y)

    def inbounds(self, p: tuple[float, float]) -> bool:
        return (
            p[0] >= self.bounds[0][0] and
            p[0] <= self.bounds[0][0] + self.bounds[1][0] and
            p[1] >= self.bounds[0][1] and
            p[1] <= self.bounds[0][1] + self.bounds[1][1]
        )

cases = int(sys.stdin.readline().rstrip())

for case_num in range(cases):
    info = sys.stdin.readline().rstrip().split(SEPARATOR)
    spy = (int(info[0]), int(info[1]))
    camera = (int(info[2]), int(info[3]))
    n_walls = int(info[4])
    
    spy_line = Line(spy, camera)

    seen = False

    for _ in range(n_walls):
        line = sys.stdin.readline().rstrip().split(SEPARATOR)

        wall_start = (int(line[0]), int(line[1]))
        wall_end = (int(line[2]), int(line[3]))

        wall_line = Line(wall_start, wall_end)

        intersect = spy_line.intersection(wall_line)

        if intersect == None or not wall_line.inbounds(intersect):
            seen = True
            break

    if seen:
        print("YES")
    else:
        print("NO")