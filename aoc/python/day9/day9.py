from functools import reduce
from typing import Any
from typing import List


class Coordinate:
    left: Any = None
    right: Any = None
    up: Any = None
    down: Any = None
    value: int
    counted_for_basin = False

    def __init__(self, value):
        self.value = value

    def is_lowest_point(self):
        if ((not self.left) or (self.value < self.left.value)) and \
                ((not self.right) or (self.value < self.right.value)) and \
                ((not self.up) or (self.value < self.up.value)) and \
                ((not self.down) or (self.value < self.down.value)):
            return True
        return False

    def basin_size(self):
        if not self.counted_for_basin and self.value != 9:
            basin = 1
            self.counted_for_basin = True
            if self.left:
                basin += self.left.basin_size()
            if self.right:
                basin += self.right.basin_size()
            if self.up:
                basin += self.up.basin_size()
            if self.down:
                basin += self.down.basin_size()
            return basin
        return 0


def puzzle1(coordinates: List[List[Coordinate]]) -> List:
    lowest_points = get_lowest_points(coordinates)
    return lowest_points


def puzzle2(lowest_points: List) -> int:
    basin_sizes = [x.basin_size() for x in lowest_points]
    return reduce(lambda x, y: x * y, list(sorted(basin_sizes, reverse=True))[:3])


def get_lowest_points(coordinates: List[List[Coordinate]]):
    return [x for coords in coordinates for x in coords if x.is_lowest_point()]


def create_coordinates(height_map: List[List[str]]):
    coordinates = []
    max_size = len(height_map)
    for y in range(max_size):
        tmp_coords = []
        for x in range(max_size):
            coord = Coordinate(int(height_map[x][y]))
            if x > 0:
                tmp_coords[x - 1].right = coord
                coord.left = tmp_coords[x - 1]
            if y > 0:
                coordinates[y - 1][x].up = coord
                coord.down = coordinates[y - 1][x]
            tmp_coords.append(coord)
        coordinates.append(tmp_coords)
    return coordinates


def read_input(path: str) -> List[List[str]]:
    with open(path, "r") as f:
        inputs = f.readlines()
        return [list(x) for x in inputs]


if __name__ == "__main__":
    heightmap = read_input("./input.txt")
    all_coords = create_coordinates(heightmap)
    lowest_points = puzzle1(all_coords)
    answer2 = puzzle2(lowest_points)
    print(f"The answer to day 9 puzzle 1: {len(lowest_points) + sum([x.value for x in lowest_points])}")
    print(f"The answer to day 9 puzzle 2: {answer2}")
