import numpy as np


def read_input(path: str):
    with open(path, "r") as f:
        lines: list = f.readlines()
    instructions = []
    for line in lines:
        splits: list = line.split(" -> ")
        instructions.append([list(map(lambda el: int(el), s.split(","))) for s in splits])
    return instructions


def fill_hor_or_vert(grid: np.ndarray, instruction: list):
    if instruction[0][0] == instruction[1][0]:
        from_point = min(instruction[0][1], instruction[1][1])
        to_point = max(instruction[0][1], instruction[1][1]) + 1
        grid[instruction[0][0], from_point:to_point] += 1
        return True
    elif instruction[0][1] == instruction[1][1]:
        from_point = min(instruction[0][0], instruction[1][0])
        to_point = max(instruction[0][0], instruction[1][0]) + 1
        grid[from_point:to_point, instruction[0][1]] += 1
        return True
    return False


def get_direction(instruction: list):
    if instruction[0][0] > instruction[1][0] and instruction[0][1] > instruction[1][1]:
        return -1, -1
    elif instruction[0][0] < instruction[1][0] and instruction[0][1] > instruction[1][1]:
        return 1, -1
    elif instruction[0][0] > instruction[1][0] and instruction[0][1] < instruction[1][1]:
        return -1, 1
    else:
        return 1, 1


def fill_diag(grid: np.ndarray, instruction: list):
    dir_x, dir_y = get_direction(instruction)
    for i in range(abs(instruction[0][0] - instruction[1][0]) + 1):
        grid[instruction[0][0] + (i * dir_x), instruction[0][1] + (i * dir_y)] += 1


def puzzle1(instructions: list):
    grid = np.zeros((1000, 1000))
    for instruction in instructions:
        fill_hor_or_vert(grid, instruction)
    return len(np.where(grid >= 2)[0])


def puzzle2(instructions: list):
    grid = np.zeros((1000, 1000))
    for instruction in instructions:
        if not fill_hor_or_vert(grid, instruction):
            fill_diag(grid, instruction)
    return len(np.where(grid >= 2)[0])


if __name__ == "__main__":
    instruction_input = read_input("./input.txt")
    print(f"The answer to day 5 puzzle 1: {puzzle1(instruction_input)}")
    print(f"The answer to day 5 puzzle 2: {puzzle2(instruction_input)}")
