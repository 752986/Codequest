import sys

SEPARATOR = " "

cases = int(sys.stdin.readline().rstrip())

class Point:
    def __init__(self, coords: str) -> None:
        pass

for case_num in range(cases):
    n_planes = int(sys.stdin.readline().rstrip())

    for i in range(n_planes):
        plane_name = sys.stdin.readline().rstrip()
        plane_name = Point(sys.stdin.readline().rstrip())

    