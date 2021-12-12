from typing import List, Any


class Grid:
    left: Any = None
    right: Any = None
    up: Any = None
    down: Any = None
    left_up: Any = None
    left_down: Any = None
    right_up: Any = None
    right_down: Any = None
    value: int
    has_flashed = False

    def __init__(self, value):
        self.value = value

    def flash_or_do_nothing(self):
        if not self.has_flashed and self.value == 10:
            self.has_flashed = True
            self.value = 0
            if self.left:
                self.left.neighbour_flashed()
            if self.right:
                self.right.neighbour_flashed()
            if self.up:
                self.up.neighbour_flashed()
            if self.down:
                self.down.neighbour_flashed()
            if self.left_up:
                self.left_up.neighbour_flashed()
            if self.left_down:
                self.left_down.neighbour_flashed()
            if self.right_up:
                self.right_up.neighbour_flashed()
            if self.right_down:
                self.right_down.neighbour_flashed()

    def neighbour_flashed(self):
        if not self.has_flashed and self.value != 10:
            self.value += 1
            self.flash_or_do_nothing()


def create_grid(grid: List[List[str]]) -> List[List[Grid]]:
    full_grid = []
    max_size = len(grid)
    for y in range(max_size):
        tmp_grid = []
        for x in range(max_size):
            grid_point = Grid(int(grid[x][y]))
            if x > 0:
                tmp_grid[x - 1].right = grid_point
                grid_point.left = tmp_grid[x - 1]
            if y > 0:
                full_grid[y - 1][x].up = grid_point
                grid_point.down = full_grid[y - 1][x]
                if x < max_size - 1:
                    full_grid[y - 1][x + 1].left_up = grid_point
                    grid_point.right_down = full_grid[y - 1][x + 1]
            if x > 0 and y > 0:
                full_grid[y - 1][x - 1].right_up = grid_point
                grid_point.left_down = full_grid[y - 1][x - 1]

            tmp_grid.append(grid_point)
        full_grid.append(tmp_grid)
    return full_grid


def take_step(grid: List[Grid]) -> int:
    flashes = 0
    for point in grid:
        point.has_flashed = False
        point.value += 1
    for point in grid:
        point.flash_or_do_nothing()
    for point in grid:
        flashes += point.value == 0
    return flashes


def puzzle1(grid: List[Grid]) -> int:
    flashes = 0
    for _ in range(100):
        flashes += take_step(grid)
    return flashes


def puzzle2(grid: List[Grid]) -> int:
    for i in range(1, 10000):
        flashes = take_step(grid)
        if flashes == 100:
            return i
    return 0


def read_input(path: str) -> List[List[str]]:
    with open(path, "r") as f:
        inputs = f.readlines()
        return [list(x) for x in inputs]


if __name__ == "__main__":
    grid_input = read_input("./input.txt")
    grid_list = [x for y in create_grid(grid_input) for x in y]
    answer1 = puzzle1(grid_list)
    grid_list = [x for y in create_grid(grid_input) for x in y]
    answer2 = puzzle2(grid_list)
    print(f"The answer to day 11 puzzle 1: {answer1}")
    print(f"The answer to day 11 puzzle 2: {answer2}")
