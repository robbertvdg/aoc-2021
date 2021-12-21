from typing import List, Tuple

from tqdm import tqdm


def enhance(coords: dict, binary_match_string: str, outer_value: str, min_x: int, max_x: int,
            min_y: int, max_y: int) -> dict:
    neighbours = [(-1, -1), (0, -1), (1, -1), (-1, 0), (0, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
    new_coords = {}
    for i in range(min_x - 1, max_x + 2):
        for j in range(min_y - 1, max_y + 2):
            bin_string = ""
            for neighbour in neighbours:
                tmp_coord = (i + neighbour[0], j + neighbour[1])
                if tmp_coord[0] < min_x or tmp_coord[0] > max_x or tmp_coord[1] < min_y or tmp_coord[1] > max_y:
                    bin_string += outer_value
                elif tmp_coord in coords:
                    bin_string += "1"
                else:
                    bin_string += "0"
            index = int(bin_string, 2)
            value = binary_match_string[index]
            if value == "#":
                new_coords[(i, j)] = 1
    return new_coords


def puzzle(coords: dict, binary_match_string: str, n=2) -> int:
    outer_value = "0"
    x_sorted = sorted(coords)
    y_sorted = sorted(coords, key=lambda x: x[1])
    max_x = x_sorted[-1][0]
    min_x = x_sorted[0][0]
    max_y = y_sorted[-1][1]
    min_y = y_sorted[0][1]
    for _ in tqdm(range(n)):
        coords = enhance(coords, binary_match_string, outer_value, min_x, max_x, min_y, max_y)
        outer_index = int(outer_value * 9, 2)
        outer_value = "1" if binary_match_string[outer_index] == "#" else "0"
        min_x -= 1
        max_x += 1
        min_y -= 1
        max_y += 1
    return len(coords)


def create_coords(grid: List[str]) -> dict:
    coords = {}
    for i, grid_str in enumerate(grid):
        for j, c in enumerate(grid_str):
            if c == "#":
                coords[(j, i)] = 1
    return coords


def read_input(path: str) -> Tuple[str, List]:
    with open(path, "r") as f:
        inputs = f.readlines()
        binary_match_string = inputs[0].strip()
        puzzle_grid = [x.strip() for x in inputs[2:]]
        return binary_match_string, puzzle_grid


if __name__ == "__main__":
    binary_string, grid_input = read_input("./input.txt")
    input_coords = create_coords(grid_input)
    answer1 = puzzle(input_coords, binary_string, 2)
    answer2 = puzzle(input_coords, binary_string, 50)
    print(f"The answer to day 20 puzzle 1: {answer1}")
    print(f"The answer to day 20 puzzle 2: {answer2}")
